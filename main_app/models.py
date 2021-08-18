from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=75)
    img = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    bio = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    img = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    #listing_date = models.DateTimeField(default=now)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name



#image list per model
# class PropertyImage(models.Model):
#     property = models.ForeignKey(Property, related_name='images')
#     image = models.ImageField()