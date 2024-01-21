from django.db import models


class Notes(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.name, self.content
