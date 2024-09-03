from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_recipe.controller.views import UserRecipeView

router = DefaultRouter()
router.register(r'user_recipe', UserRecipeView, basename='user_recipe')

urlpatterns = [
    path('', include(router.urls)),
    path('create-recipe', UserRecipeView.as_view({'post': 'createUserRecipe'}), name='create-recipe'),
    path('get-recipe', UserRecipeView.as_view({'get': 'getUserRecipe'}), name='get-recipe'),
    path('delete-recipe', UserRecipeView.as_view({'delete': 'deleteUserRecipe'}), name='delete-recipe'),
    ]