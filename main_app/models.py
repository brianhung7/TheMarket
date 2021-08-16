from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    img = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    listing_date = models.DateTimeField(auto_now_add=True)


class Seller(models.Model):
    name = models.CharField(max_length=75)
    img = models.CharField(max_length=300)
    bio = models.TextField(max_length=500)

#image list per model
# class PropertyImage(models.Model):
#     property = models.ForeignKey(Property, related_name='images')
#     image = models.ImageField()