from django.db import models
import recipes.models.recipe
import recipes.models.recipe_ingredient

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def user_can_make(self, user):
        r = []
        for recipe in recipes.models.recipe.Recipe.objects.iterator():
            if recipe.user_can_make(user):
                for ri in recipes.models.recipe_ingredient.RecipeIngredient.objects.filter(recipe=recipe):
                    if ri.ingredient.id == self.id:
                        r.append(recipe)
        return r

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id