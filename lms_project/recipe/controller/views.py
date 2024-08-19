from rest_framework import viewsets, status
from rest_framework.response import Response

from recipe.entity.recipe_content import RecipeContent
from recipe.entity.recipe_ingredient import RecipeIngredient
from recipe.entity.recipe_title import RecipeTitle


class RecipeView(viewsets.ViewSet):
    queryset = RecipeTitle.objects.all()