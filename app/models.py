from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'

class Ingredient(models.Model):
    name  = models.CharField(max_length=30)
    notes = models.TextField()
    category = models.ForeignKey(Category, related_name='ingredient', on_delete=models.CASCADE)

    def __str__(self):
        return self.name