from django.db import models

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('recipes.Ingredient', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.recipe.name + ": " + self.ingredient.name)

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
