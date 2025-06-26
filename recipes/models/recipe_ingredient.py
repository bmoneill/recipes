from django.db import models

class RecipeIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE, null=False)
    ingredient = models.ForeignKey('recipes.Ingredient', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.recipe.name + ": " + self.ingredient.name)

    def __eq__(self, other):
        if other == None:
            return False
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
