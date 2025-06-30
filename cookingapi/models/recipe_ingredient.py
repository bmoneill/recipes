"""
This module defines the RecipeIngredient model for the recipes application.

The RecipeIngredient model represents an ingredient used in a recipe with a
specific quantity.
"""

from django.db import models

class RecipeIngredient(models.Model):
    """Model representing an ingredient used in a recipe with a specific quantity."""

    UNIT_CHOICES = (
        ('unit', ''),
        ('tsp', 'Teaspoon'),
        ('dsp', 'Dessertspoon'),
        ('tbsp', 'Tablespoon'),
        ('floz', 'Fluid Ounce'),
        ('cup', 'Cup'),
        ('pt', 'Pint'),
        ('qt', 'Quart'),
        ('gal', 'Gallon'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        ('g', 'Gram'),
        ('mg', 'Milligram'),
        ('clov', 'Clove'),
    )

    UNITS = {
        'unit': {
            'long_single': '',
            'short_single': '',
            'long_plural': '',
            'short_plural': ''
        },
        'tsp': {
            'long_single': 'teaspoon',
            'short_single': 'tsp',
            'long_plural': 'teaspoons',
            'short_plural': 'tsp',
        },
        'dsp': {
            'long_single': 'dessertspoon',
            'short_single': 'dsp',
            'long_plural': 'dessertspoons',
            'short_plural': 'dsp',
        },
        'tbsp': {
            'long_single': 'tablespoon',
            'short_single': 'tbsp',
            'long_plural': 'tablespoons',
            'short_plural': 'tbsp',
        },
        'floz': {
            'long_single': 'fluid ounce',
            'short_single': 'fl. oz.',
            'long_plural': 'fluid ounces',
            'short_plural': 'fl. oz.',
        },
        'cup': {
            'long_single': 'cup',
            'short_single': 'cup',
            'long_plural': 'cups',
            'short_plural': 'cups',
        },
        'pt': {
            'long_single': 'pint',
            'short_single': 'pt',
            'long_plural': 'pints',
            'short_plural': 'pt',
        },
        'qt': {
            'long_single': 'quart',
            'short_single': 'qt',
            'long_plural': 'quarts',
            'short_plural': 'qt',
        },
        'gal': {
            'long_single': 'gallon',
            'short_single': 'gal',
            'long_plural': 'gallons',
            'short_plural': 'gal',
        },
        'l': {
            'long_single': 'liter',
            'short_single': 'l',
            'long_plural': 'liters',
            'short_plural': 'l',
        },
        'ml': {
            'long_single': 'milliliter',
            'short_single': 'ml',
            'long_plural': 'milliliters',
            'short_plural': 'ml',
        },
        'g': {
            'long_single': 'gram',
            'short_single': 'g',
            'long_plural': 'grams',
            'short_plural': 'g',
        },
        'mg': {
            'long_single': 'milligram',
            'short_single': 'mg',
            'long_plural': 'milligrams',
            'short_plural': 'mg',
        },
        'clov': {
            'long_single': 'clove',
            'short_single': 'clove',
            'long_plural': 'cloves',
            'short_plural': 'cloves',
        },
    }


    id = models.AutoField(primary_key=True, null=False)
    recipe = models.ForeignKey('cookingapi.Recipe', on_delete=models.CASCADE, null=False)
    ingredient = models.ForeignKey('cookingapi.Ingredient', on_delete=models.CASCADE,
                                   null=False)
    unit = models.CharField(max_length=4, choices=list(UNIT_CHOICES), null=False, default='unit')
    amount = models.FloatField(null=True, default=1.0)

    def short_str(self) -> str:
        """Returns a short string representation of the recipe ingredient."""
        return f"{self.ingredient.name} ({self.short_quantity_str()})"

    def long_str(self) -> str:
        """Returns a long string representation of the recipe ingredient."""
        return f"{self.ingredient.name} ({self.long_quantity_str()})"

    def short_quantity_str(self) -> str:
        """Returns a short string representation of the recipe ingredient."""
        amount = self.amount
        if amount.is_integer():
            amount = int(amount)

        if self.unit == "unit":
            return f"{amount}"
        elif self.amount != 1:
            return f"{self.amount} {self.UNITS[self.unit]['short_plural']}"
        return f"{self.amount} {self.UNITS[self.unit]['short_single']}"

    def long_quantity_str(self) -> str:
        """Returns a long string representation of the recipe ingredient."""
        amount = self.amount
        if amount.is_integer():
            amount = int(amount)

        if self.unit == "unit":
            return f"{amount}"
        elif self.amount != 1:
            return f"{self.amount} {self.UNITS[self.unit]['long_plural']}"
        return f"{self.amount} {self.UNITS[self.unit]['long_single']}"

    def __str__(self) -> str:
        return self.short_str()

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
