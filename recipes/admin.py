from django.contrib import admin
from .models.recipe import Recipe
from .models.ingredient import Ingredient
from .models.recipe_ingredient import RecipeIngredient
from .models.user_ingredient import UserIngredient

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(UserIngredient)
