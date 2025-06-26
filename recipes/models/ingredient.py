from django.db import models
from recipes.models.recipe import Recipe
from recipes.models.recipe_ingredient import RecipeIngredient

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)

    def user_can_make(self, user) -> list[Recipe]:
        return [
            recipe
            for recipe in Recipe.objects.iterator()
            if recipe.user_can_make(user)
            and RecipeIngredient.objects.filter(recipe=recipe, ingredient=self).exists()
        ]

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if other == None:
            return False
        return self.id == other

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id