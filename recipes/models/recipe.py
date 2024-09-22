from django.db import models
from .recipe_ingredient import RecipeIngredient
from .user_ingredient import UserIngredient

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def user_can_make(self, user):
        for ri in RecipeIngredient.objects.filter(recipe=self):
            ingredient = ri.ingredient
            if not UserIngredient.objects.filter(user=user, ingredient=ingredient).exists():
                return False
        return True

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id