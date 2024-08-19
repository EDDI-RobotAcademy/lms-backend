from django.db import models

class AccountTicket(models.Model):
    Ticket = models.IntegerField(default=99999)

    def __str__(self):
        return self.Ticket

    class Meta:
        db_table = 'account_ticket'
        app_label = 'account'