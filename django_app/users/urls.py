from django.urls import path, include

from .views import profile_update

urlpatterns = [
    path('', profile_update, name="profile"),
]