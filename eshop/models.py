from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=200)
    Specs = models.CharField(max_length=200)
    Brand = models.CharField(max_length=200)

    def __str__(self):
        return self.ProductName
    


class Cart(models.Model):
    Name = models.CharField(max_length=200)
    Specs = models.CharField(max_length=200)
    Brand = models.CharField(max_length=200)
    
