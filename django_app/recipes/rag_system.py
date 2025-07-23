import os
from typing import List, Dict
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from groq import Groq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.llms.base import LLM
from django.conf import settings
from .models import Recipe
from dotenv import load_dotenv
# loading secret variables in .env
load_dotenv()

class GroqLLM(LLM):
    """Wrapper LangChain pour Groq"""
    
    def __init__(self, api_key: str, model: str = "mixtral-8x7b-32768"):
        super().__init__()
        self.client = Groq(api_key=os.getenv("API_KEY_GROQ"))
        self.model = model
    
    def _call(self, prompt: str, stop=None, run_manager=None) -> str:
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erreur lors de la génération de la réponse: {str(e)}"
    
    @property
    def _llm_type(self) -> str:
        return "groq"


class RecipeRAGSystem:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vectorstore = None
        self.qa_chain = None
        self.setup_rag_system()
    
    def get_recipe_documents(self) -> List[Document]:
        """Récupère toutes les recettes et les convertit en documents"""
        recipes = Recipe.objects.all()
        documents = []
        
        for recipe in recipes:
            # Créer le contenu du document avec toutes les informations de la recette
            content = f"""
            Titre: {recipe.title}
            De saison: {recipe.season}
            Catégorie: {recipe.category}
            tags: {recipe.tags}
            Durée: {recipe.duration}
            Difficulté: {recipe.level}
            Portions: {recipe.persons_number}
            Coût: {recipe.cost}
            Ingrédients: {recipe.ingredients}
            Instructions: {recipe.steps}
            """
            
            # Métadonnées pour récupérer les informations de la recette
            metadata = {
                'id': recipe.id,
                'title': recipe.title,
                'image_url': recipe.image_url,
                'season': recipe.season,
                'category': recipe.category,
                'tags': recipe.tags,
                'duration': recipe.duration,
                'level': recipe.level,
                'cost': recipe.cost,
                'persons_number': recipe.persons_number,
                'ingredients': recipe.ingredients,
                'steps': recipe.steps, 
            }
            
            documents.append(Document(page_content=content, metadata=metadata))
        
        return documents
    
    def setup_rag_system(self):
        """Configure le système RAG"""
        try:
            # Récupérer les documents des recettes
            documents = self.get_recipe_documents()
            
            if not documents:
                print("Aucune recette trouvée dans la base de données")
                return
            
            # Diviser les documents si nécessaire
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            splits = text_splitter.split_documents(documents)
            
            # Créer le vectorstore
            self.vectorstore = FAISS.from_documents(splits, self.embeddings)
            
            # Configurer le prompt personnalisé
            prompt_template = """
            Tu es un assistant culinaire expert. Utilise les informations suivantes sur les recettes pour répondre à la question de l'utilisateur.
            
            Contexte des recettes:
            {context}
            
            Question: {question}
            
            Instructions:
            - Réponds en français
            - Recommande des recettes spécifiques basées sur la question
            - Pour chaque recette recommandée, fournis:
              * Le nom exact de la recette
              * Un lien vers la recette au format: http://127.0.0.1:8000//recipes/[id]/
              * Une brève explication de pourquoi cette recette correspond à la demande
            - Si aucune recette ne correspond, suggère des alternatives ou demande plus de précisions
            - Sois amical et utile
            
            Réponse:
            """
            
            PROMPT = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            
            # Créer la chaîne QA (utilise un modèle local si GROQ n'est pas configuré)
            try:
                if hasattr(settings, 'GROQ_API_KEY') and settings.GROQ_API_KEY != 'your-groq-api-key-here':
                    llm = GroqLLM(api_key=settings.GROQ_API_KEY)
                else:
                    # Pas de clé Groq configurée, utiliser une réponse basique
                    llm = None
            except:
                llm = None
            
            if llm:
                self.qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff",
                    retriever=self.vectorstore.as_retriever(search_kwargs={"k": 3}),
                    chain_type_kwargs={"prompt": PROMPT}
                )
            
        except Exception as e:
            print(f"Erreur lors de la configuration du système RAG: {e}")
    
    def get_recipe_recommendations(self, question: str) -> str:
        """Obtient des recommandations de recettes basées sur la question"""
        try:
            if not self.vectorstore:
                return "Désolé, le système de recommandations n'est pas disponible pour le moment."
            
            # Si Groq est configuré, utiliser la chaîne QA
            if self.qa_chain:
                response = self.qa_chain.run(question)
                return response
            
            # Sinon, utiliser une recherche de similarité basique
            docs = self.vectorstore.similarity_search(question, k=3)
            
            if not docs:
                return "Je n'ai pas trouvé de recettes correspondant à votre recherche. Pouvez-vous être plus précis ?"
            
            response = "Voici les recettes que je recommande :\n\n"
            
            for doc in docs:
                metadata = doc.metadata
                recipe_id = metadata.get('id')
                title = metadata.get('title')
                level = metadata.get('level')
                prep_time = metadata.get('duration')
                
                response += f"🍽️ **{title}**\n"              
                response += f"   Difficulté: {level}\n"
                response += f"   Temps de préparation: {prep_time}\n\n"
                response += f"   Lien: http://127.0.0.1:8000/recipes/{recipe_id}/\n"
            
            return response
            
        except Exception as e:
            return f"Désolé, une erreur s'est produite: {str(e)}"
    
    def refresh_data(self):
        """Actualise les données du système RAG"""
        self.setup_rag_system()

# Instance globale du système RAG
rag_system = RecipeRAGSystem()