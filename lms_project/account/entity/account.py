from django.db import models

from account.entity.account_login_type import AccountLoginType

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    loginType = models.ForeignKey(AccountLoginType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'
        app_label = 'account'
