from rest_framework import viewsets
from cookingapi.models import Recipe
from cookingapi.serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
