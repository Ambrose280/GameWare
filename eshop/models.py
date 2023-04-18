from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    Name = models.CharField(max_length=200)
    Specs = models.CharField(max_length=200)
    Brand = models.CharField(max_length=200)
    Price = models.IntegerField(default=0)
    Image = models.ImageField(null=True)


    def __str__(self):
        return self.Name
    


class Cart(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_products")
    Name = models.CharField(max_length=200)
    Specs = models.CharField(max_length=200)
    Brand = models.CharField(max_length=200)
    Image = models.ImageField(null=True)
    Price = models.IntegerField(default=0)

    def __str__(self):
        return self.Name
    
