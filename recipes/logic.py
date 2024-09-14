"""
TODO
"""
from .models import Recipe, UserIngredient, RecipeIngredient

def available_recipes(user):
    """
    TODO
    """
    recipes = []
    for recipe in Recipe.objects.iterator():
        if recipe.user_can_make(user):
            recipes.append(recipe)
    return recipes
