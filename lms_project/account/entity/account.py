from django.db import models

from account.entity.account_login_type import AccountLoginType
from account.entity.account_paid_member_type import AccountPaidMemberType


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    loginType = models.ForeignKey(AccountLoginType, on_delete=models.CASCADE)
    paidmemberType = models.ForeignKey(AccountPaidMemberType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'
        app_label = 'account'
