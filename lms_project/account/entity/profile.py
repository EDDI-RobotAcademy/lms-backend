from django.db import models

class Profile(models.Model):
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64, default="n")

    class Meta:
        db_table = 'profile'