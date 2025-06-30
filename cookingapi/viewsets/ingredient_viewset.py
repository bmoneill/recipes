from rest_framework import viewsets
from cookingapi.models import Ingredient
from cookingapi.serializers import IngredientSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
