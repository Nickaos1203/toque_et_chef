from django.core.management.base import BaseCommand
from recipes.rag_system import rag_system

class Command(BaseCommand):
    help = 'Actualise les données du système RAG avec les nouvelles recettes'

    def handle(self, *args, **options):
        self.stdout.write('Actualisation du système RAG...')
        rag_system.refresh_data()
        self.stdout.write(
            self.style.SUCCESS('Système RAG actualisé avec succès!')
        )