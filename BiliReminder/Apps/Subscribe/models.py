from django.db import models


# Create your models here.

class UpLoader(models.Model):
    uid = models.CharField(max_length=10)
    pass

