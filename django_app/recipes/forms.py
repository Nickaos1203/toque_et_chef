from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "image_url", "category", "duration", "level", "cost", "number", "persons_number"]

    def save(self, commit=True):
        instance = super().save(commit=False)

        request_data = self.data
        ingredients_inputs = []
        steps_inputs = []

        for item in request_data:
            if item.startswith("step_") and request_data[item].strip():             # liste des ingrédients
                steps_inputs.append(request_data[item].strip())
            if item.startswith("ingredient_") and request_data[item].strip():       # Liste des étapes
                ingredients_inputs.append(request_data[item].strip())
        
        instance.ingredients = ";".join(ingredients_inputs)                        # concaténation des ingrédients avec ";"
        instance.steps = ";".join(steps_inputs)                                    # concaténation des étapes avec ";"

        if commit:
            instance.save()
        return instance


