"""
This module defines the RecipesUser model, which extends Django's AbstractUser.

It includes methods for checking available recipes, ingredients, and
unavailable recipes for a user.

In the future, dietary restrictions, dietary preferences, currency, and region
should be added to enhance the user experience.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from .recipe_ingredient import RecipeIngredient
from .user_ingredient import UserIngredient
from .recipe import Recipe

class CookingAPIUser(AbstractUser):
    """Model representing a user in the recipes application."""
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(max_length = 50, unique = True)
    full_name = models.CharField(max_length = 5)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def available_recipes(self):
        """Returns a list of recipes that the user can make."""
        return [
            recipe
            for recipe in Recipe.objects.iterator()
            if recipe.user_can_make(self)
        ]

    def has_ingredient(self, ingredient):
        """Returns True if the user has the specified ingredient."""
        return UserIngredient.objects.filter(ingredient=ingredient).exists()

    def num_missing_ingredients(self, recipe):
        """Returns the number of ingredients the user is missing for a recipe."""
        return sum(
            1 for ri in RecipeIngredient.objects.filter(recipe=recipe)
            if not self.has_ingredient(ri.ingredient)
        )


    def unavailable_recipes(self):
        """Returns a list of recipes that the user cannot make, along with the number of missing
        ingredients for that recipe."""
        return [
            (recipe, self.num_missing_ingredients(recipe))
            for recipe in Recipe.objects.iterator()
            if not recipe.user_can_make(self)
        ]

    def __str__(self):
        return f"{self.email}"
