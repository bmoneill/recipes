"""
This module defines the Price model for the recipes application.
It includes fields for the price amount, currency unit, and a foreign key to the
associated Ingredient model.

This model does not currently take into account differing prices based on
regions, retailers, or other factors, so at the moment it is essentially just a
rough estimate. Future enhancements could include adding region and retailer
fields to provide more accurate pricing information.
"""

from django.db import models

class Price(models.Model):
    """Model representing the price of an ingredient in a specific currency."""

    CURRENCY = {
        "$": "Dollar",
        "€": "Euro",
        "£": "Pound",
    }

    id = models.AutoField(primary_key=True, null=False)
    unit = models.CharField(max_length=4, choices=list(CURRENCY.items()), null=False)
    amount = models.FloatField(null=False)
    ingredient = models.ForeignKey('recipes.Ingredient', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.amount} {self.unit}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
