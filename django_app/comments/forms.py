from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'grade', 'contain']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Titre du commentaire'
            }),
            'grade': forms.NumberInput(attrs={
                'class': 'w-full p-2 border rounded',
                'min': 0,
                'max': 5,
                'step': 0.5,
                'placeholder': 'Note sur 5'
            }),
            'contain': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Ton commentaire...',
                'rows': 4
            }),
        }
