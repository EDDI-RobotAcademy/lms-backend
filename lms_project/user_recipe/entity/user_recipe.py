from django.db import models

from account.entity.account import Account


class UserRecipe(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    recipe_hash = models.CharField(max_length=64, null=False)  # SHA-256 해시값

    class Meta:
        db_table = 'user_recipe'
        unique_together = ('account_id', 'recipe_hash')  # account_id와 recipe_hash의 조합이 고유
