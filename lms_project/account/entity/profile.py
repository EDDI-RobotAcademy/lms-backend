from django.db import models

from account.entity.account import Account


class Profile(models.Model):
    email = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64, default="n")
    nickname = models.CharField(max_length=64, default="n")
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    class Meta:
        db_table = 'profile'