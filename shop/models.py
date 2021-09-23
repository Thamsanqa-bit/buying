from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=280)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=280)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=280)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    postalAddress = models.CharField(max_length=1000)
