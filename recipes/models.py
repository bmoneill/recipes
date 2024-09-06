from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class RecipeIngredient(models.Model):
    recipe = models.ManyToManyField(Recipe)
    ingredient = models.ManyToManyField(Ingredient)

class User(models.Model):
    name = models.CharField(max_length = 50)

class UserIngredient(models.Model):
    user = models.ManyToManyField(User)
    ingredient = models.ManyToManyField(Ingredient)