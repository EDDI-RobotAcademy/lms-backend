from django.db import models


class RecipeTitle(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, null=False)
    category = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"id of RecipeTitle: {self.recipe_id}"

    class Meta:
        db_table = 'recipe_title'
        app_label = 'recipe'