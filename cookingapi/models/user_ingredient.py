from django.conf import settings
from django.db import models

class UserIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    ingredient = models.ForeignKey('cookingapi.Ingredient', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.user.username}: {self.ingredient.name}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
