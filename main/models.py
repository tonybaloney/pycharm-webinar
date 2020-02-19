from django.db import models

# Create your models here.
class TemporaryUser(models.Model):
    name: str = models.fields.CharField(max_length=100)


class Product(models.Model):
    name = models.fields.CharField(max_length=100)
    price = models.fields.FloatField()
    stock = models.fields.IntegerField()
    description = models.fields.TextField()