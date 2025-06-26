from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.recipe_view, name="recipe_detail"),
    path("recipes/", views.recipes_view, name="recipes"),
    path("ingredients/", views.ingredients_view, name="ingredients"),
]
