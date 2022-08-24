from django.db import models

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    set = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    img = models.URLField()
