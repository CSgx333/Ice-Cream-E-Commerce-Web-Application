from django.db import models
from unicodedata import name

class Popular(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class New(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Cones(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Sticks(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Cake(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Mochi(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class List(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Cart(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    amount=models.IntegerField()
    image=models.CharField(max_length=50)
    def __str__(self):
        return self.name