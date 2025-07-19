from django import form
from .models import Comment

class CommentForm(form.Form):
    class Meta:
        model = Comment
        fields = ['title', 'grade', 'contain']