from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Comment
from recipes.models import Recipe
from users.models import CustomUser

from .models import CommentForm


@login_required
def comment_create(request, id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.recipe = get_object_or_404(Recipe, id=id)
        comment.author = request.user
        comment.save()
        return redirect('recipe_detail, id=id')
    else:
        form = CommentForm()
    return render(request, 'comments/comment_create.html', {'form':form})


@login_required
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('recipes-detail', id=comment.recipe.id)
    return render(request, 'comments/comment_delete.html', {'comment':comment})

@login_required
def comments_by_user(request, id):
    pass