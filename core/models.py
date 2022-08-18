from django.db import models

# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    account_name = models.CharField(max_length=100)
    website = models.URLField(max_length=255)
   


class Destination(models.Model):
    url = models.URLField(max_length=255)
    http_method = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
   


