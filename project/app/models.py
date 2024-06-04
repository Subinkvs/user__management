from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.name