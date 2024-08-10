from django.db import models

class Profile(models.Model):
    email = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'profile'