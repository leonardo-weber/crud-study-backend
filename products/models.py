from django.db import models
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - ${self.category.name}'