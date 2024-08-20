from django.db import models

class AccountCherry(models.Model):
    Cherry = models.IntegerField(default=99999)

    def __str__(self):
        return self.Cherry

    class Meta:
        db_table = 'account_cherry'
        app_label = 'account'