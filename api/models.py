from django.db import models

# Create your models here.

#create contest model

class Contest(models.Model):
    name = models.CharField(max_length=200, unique=True)
    platform = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
