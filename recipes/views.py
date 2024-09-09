"""
TODO
"""
from django.shortcuts import get_object_or_404, render
from .models import Recipe
from .logic import available_recipes

def index(request):
    """
    TODO
    """
    context = {
        "recipes": available_recipes(request.user),
        "username": request.user.username
    }
    return render(request, "recipes/index.html", context)

def recipe_detail(request, recipe_id):
    """
    TODO
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})

def user_ingredient_detail(request, ingredient_id):
    """
    TODO: Show recipes user has all ingredients for that includes ingredient_id
    """
    pass