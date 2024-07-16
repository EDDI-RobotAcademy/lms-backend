from django.db import models


class Board(models.Model):
    boardId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    content = models.TextField()


def __str__(self):
    return f"Cart -> id: {self.id}"


class Meta:
    db_table = 'board'
