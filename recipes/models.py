from django.db import models
from django.conf import settings

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def user_can_make(self, user):
        for recipe_ingredient in RecipeIngredient.objects.filter(recipe=self):
            ingredient = recipe_ingredient.ingredient
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

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def user_can_make(self, user):
        recipes = []
        for recipe in Recipe.objects.iterator():
            if recipe.user_can_make(user):
                for recipe_ingredient in RecipeIngredient.objects.filter(recipe=recipe):
                    if recipe_ingredient.ingredient.id == self.id:
                        recipes.append(recipe)
        return recipes

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return self.id == other.id

    # TODO can we genericize this into a new Model class for this application?
    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.recipe.name + ": " + self.ingredient.name)

class UserIngredient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username + ": " + self.ingredient.name)
