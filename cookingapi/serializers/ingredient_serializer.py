from rest_framework import serializers
from cookingapi.models import Ingredient

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
