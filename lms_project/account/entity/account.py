from django.db import models

from account.entity.account_cherry import AccountCherry
from account.entity.account_login_type import AccountLoginType
from account.entity.account_paid_member_type import AccountPaidMemberType
from account.entity.account_ticket import AccountTicket


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    loginType = models.ForeignKey(AccountLoginType, on_delete=models.CASCADE)
    paidmemberType = models.ForeignKey(AccountPaidMemberType, on_delete=models.CASCADE)
    Ticket = models.ForeignKey(AccountTicket, on_delete=models.CASCADE)
    Cherry = models.ForeignKey(AccountCherry, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'
        app_label = 'account'
