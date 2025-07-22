from django.urls import path, include

from .views import comment_create, comment_delete, my_comments

urlpatterns = [
    path('create/<int:id>/', comment_create, name="comment_create"),
    path('delete/<int:id>/', comment_delete, name="comment_delete"),
    path('my-comments', my_comments, name="my_comments"),
]
