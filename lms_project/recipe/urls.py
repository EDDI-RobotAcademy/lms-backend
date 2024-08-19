from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe.controller.views import RecipeView

router = DefaultRouter()
router.register(r'recipe', RecipeView, basename='recipe')

urlpatterns = [
    path('', include(router.urls)),
    ]