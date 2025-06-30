from django.db import models
"""
This module defines the Quantity model for the recipes application.
It includes fields for the quantity amount and unit of measurement.

Future enhancements could include adding support for different measurement
units.

Currently, the string representation of the Quantity model does not convert
units for display in templates, which should be addressed in the future.
"""

class Quantity(models.Model):
    """Model representing unit and quantity of an ingredient with a specific unit of measurement."""

    UNIT_CHOICES = {
        "tsp": "Teaspoon",
        "dsp": "Dessertspoon",
        "tbsp": "Tablespoon",
        "floz": "Fluid Ounce",
        "cup": "Cup",
        "pt": "Pint",
        "qt": "Quart",
        "gal": "Gallon",
        "l": "Liters",
        "ml": "Milliliters",
        "g": "Grams",
        "mg": "Milligrams",
    }

    id = models.AutoField(primary_key=True, null=False)
    unit = models.CharField(max_length=4, choices=list(UNIT_CHOICES.items()), null=False)
    amount = models.FloatField(null=False)

    def __str__(self):
        # TODO convert units when using this in templates
        return f"{self.amount}{self.unit}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
