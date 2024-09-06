from django.contrib import admin

from .models import Recipe, Ingredient, User, RecipeIngredient, UserIngredient

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(User)
admin.site.register(RecipeIngredient)
admin.site.register(UserIngredient)