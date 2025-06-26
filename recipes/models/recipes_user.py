from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
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
        recipes = []
        for recipe in Recipe.objects.iterator():
            if recipe.user_can_make(self):
                recipes.append(recipe)
        return recipes
    
    def has_ingredient(self, ingredient):
        return UserIngredient.objects.filter(ingredient=ingredient)
    
    def num_missing_ingredients(self, recipe):
        missing = 0
        for ri in RecipeIngredient.objects.iterator():
            if not self.has_ingredient(ri.ingredient):
                missing += 1
        return missing


    def unavailable_recipes(self):
        recipes = []
        for recipe in Recipe.objects.iterator():
            if not recipe.user_can_make(self):
                recipes.append((recipe, self.num_missing_ingredients(recipe)))
        return recipes

    def __str__(self):
        return "{}".format(self.email)
