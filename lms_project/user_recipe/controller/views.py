from rest_framework import viewsets, status
from rest_framework.response import Response


from user_recipe.entity.user_recipe import UserRecipe


class RecipeView(viewsets.ViewSet):
    queryset = UserRecipe.objects.all()