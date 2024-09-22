from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.recipe_view, name="recipe_detail"),
    path("available_recipes/", views.available_recipes_view, name="available_recipes"),
]