from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    note = models.ForeignKey(Notes, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


class Profile(LoginRequiredMixin, models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user)