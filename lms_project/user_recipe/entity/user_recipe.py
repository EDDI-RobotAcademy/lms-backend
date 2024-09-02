from django.db import models
from django.db.models import Max

class UserRecipe(models.Model):
    user_id = models.IntegerField(null=False)
    user_recipe_id = models.IntegerField(null=False)
    recipe_name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'user_recipe'
        app_label = 'user_recipe'
        unique_together = ('user_id', 'user_recipe_id')

    def save(self, *args, **kwargs):
        if not self.user_recipe_id:
            max_id = UserRecipe.objects.filter(user_id=self.user_id).aggregate(Max('user_recipe_id'))['user_recipe_id__max']
            self.user_recipe_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id} - {self.recipe_name}"
