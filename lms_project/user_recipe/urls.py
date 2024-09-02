from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_recipe.controller.views import RecipeView

router = DefaultRouter()
router.register(r'user_recipe', RecipeView, basename='user_recipe')

urlpatterns = [
    path('', include(router.urls)),
    ]