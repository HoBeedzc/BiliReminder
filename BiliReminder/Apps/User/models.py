from django.db import models


# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=50, null=False)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    bili_uid = models.CharField(max_length=10)

    def __str__(self):
        return self.name
