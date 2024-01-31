from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='my_notes')
    title = models.CharField(max_length=100, default='New note')
    content = models.TextField(max_length=1000)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


