"""
This module defines the Ingredient model for the recipes application.

Future enhancements could include adding fields for ingredient type, allergen
information, flavor profile, or other characteristics to enable more advanced
recipe matching and suggestions.
"""

from django.db import models
from . import Recipe
from . import RecipeIngredient

class Ingredient(models.Model):
    """Model representing an ingredient used in recipes."""

    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)

    def user_can_make(self, user) -> list[Recipe]:
        """ Check what recipes the user can make that contain this ingredient. """

        return [
            recipe
            for recipe in Recipe.objects.iterator()
            if recipe.user_can_make(user)
            and RecipeIngredient.objects.filter(recipe=recipe, ingredient=self).exists()
        ]

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        if other is None:
            return False
        return self.id == other

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
