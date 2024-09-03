from django.db import models

class UserRecipe(models.Model):
    account_id = models.IntegerField(null=False)
    user_recipe_id = models.IntegerField(null=False)

    class Meta:
        db_table = 'user_recipe'
        unique_together = ('account_id', 'user_recipe_id')
