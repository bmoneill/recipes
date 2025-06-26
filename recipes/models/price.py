from django.db import models

class Price(models.Model):
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
