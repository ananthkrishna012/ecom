
from django.db import models

class Product(models.Model):  
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()

class add(models.Model):
    name=models.CharField(max_length=200,null=True)
  
    email=models.CharField(max_length=200)
    
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

class History(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    add=models.ForeignKey(add,on_delete=models.CASCADE)
    date=models.DateField()