from django.db import models
from django.conf import settings

class Recipe(models.Model):
    """
    TODO
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.name)

class Ingredient(models.Model):
    """
    TODO
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class RecipeIngredient(models.Model):
    """
    TODO
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.recipe.name + ": " + self.ingredient.name)

class UserIngredient(models.Model):
    """
    TODO
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username + ": " + self.ingredient.name)
