from django.db import models

class Board(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Cart -> id: {self.id}"

    class Meta:
        db_table = 'board'