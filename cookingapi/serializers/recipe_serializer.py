from rest_framework import serializers
from cookingapi.models import Recipe, RecipeIngredient
from cookingapi.serializers.ingredient_serializer import IngredientSerializer

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the Recipe model."""

    name = serializers.CharField(max_length=100)
    author = serializers.CharField(source='author.username', read_only=True)
    description = serializers.CharField(max_length=2000)
    ingredients = serializers.SerializerMethodField()
    time = serializers.DurationField(default=None, allow_null=True)

    class Meta:
        model = Recipe
        fields = ['name', 'author', 'description', 'ingredients', 'time']

    def get_ingredients(self, obj):
        """Returns a list of ingredients for the recipe."""
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=obj)
        ingredients = [ri.ingredient for ri in recipe_ingredients]
        return IngredientSerializer(ingredients, many=True).data
