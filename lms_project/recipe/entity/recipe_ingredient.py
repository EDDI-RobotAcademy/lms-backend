from django.db import models

from recipe.entity.recipe_title import RecipeTitle


class RecipeIngredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient = models.TextField(null=False)
    plate = models.IntegerField(null=False)
    recipe_id = models.OneToOneField(RecipeTitle, on_delete=models.CASCADE, db_column='recipe_id')

    def __str__(self):
        return f"id of RecipeIngredient: {self.ingredient_id}"

    class Meta:
        db_table = 'recipe_ingredient'
        app_label = 'recipe'