from django.db import models


class AccountLoginType(models.Model):
    class LoginType(models.TextChoices):
        NORMAL = 'NORMAL', 'Normal'
        GOOGLE = 'GOOGLE', 'Google'

    loginType = models.CharField(max_length=10, choices=LoginType.choices, default=LoginType.NORMAL)

    def __str__(self):
        return self.loginType

    class Meta:
        db_table = 'account_login_type'
        app_label = 'account'