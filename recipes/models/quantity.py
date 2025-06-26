from django.db import models

class Quantity(models.Model):
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

    # TODO convert units when using this in templates
    def __str__(self):
        return f"{self.amount}{self.unit}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
