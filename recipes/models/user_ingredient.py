from django.conf import settings
from django.db import models

class UserIngredient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredient = models.ForeignKey('recipes.Ingredient', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username + ": " + self.ingredient.name)

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id