"""
This module defines the Recipe model for the recipes application.

Tags must be added in the future to allow for filtering recipes.
"""

from django.conf import settings
from django.db import models

class Recipe(models.Model):
    """Model representing a recipe with its author, description, and time needed to make."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=2000)
    time = models.DurationField(default=None, null=True)
    ingredients = models.ManyToManyField(
        'cookingapi.Ingredient',
        through='cookingapi.RecipeIngredient',
        related_name='recipes'
    )

    def user_can_make(self, user) -> bool:
        """Returns True if user has all Ingredients needed to make this Recipe"""

        missing = RecipeIngredient.objects.filter(
            recipe=self
        ).exclude(
            ingredient__in=UserIngredient.objects.filter(user=user)
                .values('ingredient')
        )
        return not missing.exists()

    def user_can_almost_make(self, user, quota) -> bool:
        """
        Returns True if user is missing quota or less Ingredients needed
        to make this Recipe
        """

        for ri in self.ingredients.all():
            ingredient = ri.ingredient
            if not UserIngredient.objects.filter(user=user, ingredient=ingredient).exists():
                quota -= 1
                if quota < 0:
                    return False
        return quota >= 0

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.id == other

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
