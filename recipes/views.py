from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Recipe

def index(request):
    context = {
        "recipes": Recipe.objects.order_by("-name")
    }
    return render(request, "recipes/index.html", context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})