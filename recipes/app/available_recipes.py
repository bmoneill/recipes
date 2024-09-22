from recipes.models.recipe import Recipe

def available_recipes(user):
    recipes = []
    for recipe in Recipe.objects.iterator():
        if recipe.user_can_make(user):
            recipes.append(recipe)
    return recipes