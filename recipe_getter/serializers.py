from rest_framework import serializers
from .models import RecipeData, Ingredient


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecipeData
        fields = ('name', 'meal_type', 'address', 'ingredients', 'image_url')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', )
