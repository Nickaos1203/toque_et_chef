from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]