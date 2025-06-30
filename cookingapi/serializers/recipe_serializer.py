from rest_framework import serializers
from cookingapi.models import Recipe
from . import IngredientSerializer

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Recipe model."""

    name = serializers.CharField(max_length=100)
    author = serializers.CharField(source='author.username', read_only=True)
    description = serializers.CharField(max_length=2000)

    ingredients = IngredientSerializer(many=True, read_only=True)
    time = serializers.DurationField(default=None, allow_null=True)

    class Meta:
        model = Recipe
        fields = ['name', 'author', 'description', 'ingredients', 'time']
