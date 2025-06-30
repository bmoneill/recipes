"""
This module defines the RecipeIngredient model for the recipes application.

The RecipeIngredient model represents an ingredient used in a recipe with a
specific quantity.
"""

from django.db import models

class RecipeIngredient(models.Model):
    """Model representing an ingredient used in a recipe with a specific quantity."""

    id = models.AutoField(primary_key=True, null=False)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, null=False)
    ingredient = models.ForeignKey('recipes.Ingredient', on_delete=models.CASCADE,
                                               null=False)
    quantity = models.ForeignKey('recipes.Quantity', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.recipe.name}: {self.quantity.amount} {self.ingredient.name}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
