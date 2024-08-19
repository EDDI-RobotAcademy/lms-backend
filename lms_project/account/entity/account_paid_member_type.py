from django.db import models

class AccountPaidMemberType(models.Model):
    paidmemberType = models.IntegerField(default=0)

    def __str__(self):
        return self.paidmemberType

    class Meta:
        db_table = 'account_paid_member_type'
        app_label = 'account'