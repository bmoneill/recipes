from .models import Recipe, Ingredient, UserIngredient, RecipeIngredient

def user_can_make(user, recipe):
    for recipe_ingredient in RecipeIngredient.objects.filter(recipe=recipe):
        ingredient = recipe_ingredient.ingredient
        if not UserIngredient.objects.filter(user=user, ingredient=ingredient).exists():
            return False

    return True

def available_recipes(user):
    recipes = []
    for recipe in Recipe.objects.iterator():
        if user_can_make(user, recipe):
            recipes.append(recipe)
    
    return recipes