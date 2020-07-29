import json
from django.shortcuts import render, redirect
from .models import RecipeData, Ingredient
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import IngredientInputForm, SelectMealTypeForm
from django import forms
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core import serializers


from rest_framework import viewsets
from .serializers import RecipeSerializer, IngredientSerializer
from .models import RecipeData


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = RecipeData.objects.all().order_by('name')
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer


@ensure_csrf_cookie
def process_recipes(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # extract contents and meal type from POST data
        contents = data["contents"]
        meal_type = data["meal_type"]
        # search for recipes
        all_recipes = RecipeData.objects.all()
        recipe_list = []
        for recipe in all_recipes:
            if recipe.meal_type == meal_type:
                check = all(item in contents for item in recipe.ingredients)
                if check is True:
                    recipe_list.append(recipe)
                else:
                    continue
            else:
                continue

        response = serializers.serialize("json", recipe_list)

        return JsonResponse(response, safe=False)
