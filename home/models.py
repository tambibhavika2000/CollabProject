from django.db import models
from api.models import Contest
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bookmarks = models.ManyToManyField(Contest, blank=True)

    def __str__(self):
        return self.user.username