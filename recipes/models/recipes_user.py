from django.db import models
from django.contrib.auth.models import AbstractUser
from .recipe_ingredient import RecipeIngredient
from .user_ingredient import UserIngredient
from .recipe import Recipe

class RecipesUser(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(max_length = 50, unique = True)
    full_name = models.CharField(max_length = 5)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def available_recipes(self):
        return [
            recipe
            for recipe in Recipe.objects.iterator()
            if recipe.user_can_make(self)
        ]

    def has_ingredient(self, ingredient):
        return UserIngredient.objects.filter(ingredient=ingredient).exists()

    def num_missing_ingredients(self, recipe):
        return sum(
            1 for ri in RecipeIngredient.objects.filter(recipe=recipe)
            if not self.has_ingredient(ri.ingredient)
        )


    def unavailable_recipes(self):
        return [
            (recipe, self.num_missing_ingredients(recipe))
            for recipe in Recipe.objects.iterator()
            if not recipe.user_can_make(self)
        ]

    def __str__(self):
        return f"{self.email}"
