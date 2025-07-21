from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Comment
from recipes.models import Recipe
from users.models import CustomUser

from .forms import CommentForm


@login_required
def comment_create(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_create.html', {'form':form, 'recipe':recipe})


@login_required
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id, author=request.user)
    recipe_pk = comment.recipe.id
    comment.delete()
    messages.success(request, 'Commentaire supprimé!')
    
    return redirect('my_comments')


@login_required
def my_comments(request):
    comments = Comment.objects.filter(author=request.user)
    return render(request, 'comments/my_comments.html', {'comments': comments})