from django.db import models

from recipe.entity.recipe_title import RecipeTitle


class RecipeContent(models.Model):
    content_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=512, null=False)
    recipe_id = models.OneToOneField(RecipeTitle, on_delete=models.CASCADE, db_column='recipe_id', null=False)

    def __str__(self):
        return f"id of RecipeContent: {self.content_id}"

    class Meta:
        db_table = 'recipe_content'
        app_label = 'recipe'