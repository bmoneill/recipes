from django.db import models
from .recipe_ingredient import RecipeIngredient
from .user_ingredient import UserIngredient

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def user_can_make(self, user):
        for ri in RecipeIngredient.objects.filter(recipe=self):
            ingredient = ri.ingredient
            if not UserIngredient.objects.filter(user=user, ingredient=ingredient).exists():
                return False
        return True
    
    def user_can_almost_make(self, user, quota):
        for ri in RecipeIngredient.objects.filter(recipe=self):
            ingredient = ri.ingredient
            if not UserIngredient.objects.filter(user=user, ingredient=ingredient).exists():
                quota -= 1
                if quota == 0:
                    return False
        return quota != 0
    
    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        if other == None:
            return False
        return self.id == other

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
