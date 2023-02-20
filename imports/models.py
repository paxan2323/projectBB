from django.db import models

# Create your models here.
class Config(models.Model):
    url = models.URLField()
    