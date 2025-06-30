from rest_framework import serializers
from cookingapi.models import Ingredient

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=100, allow_blank=False)

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
