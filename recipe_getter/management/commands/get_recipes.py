from django.core.management.base import BaseCommand, CommandError
from recipe_getter.models import RecipeData
from ..command_utils import ingredient_parsing as parse
from ...models import RecipeData, Ingredient
import bs4 as bs
import urllib.request
import json
import time


class Command(BaseCommand):
    categories = {
        "dessert": "https://www.allrecipes.com/recipes/79/desserts/?page=",
        "main_course": "https://www.allrecipes.com/recipes/17562/dinner/?page=",
        "breakfast": "https://www.allrecipes.com/recipes/78/breakfast-and-brunch/?page=",
        "healthy": "https://www.allrecipes.com/recipes/84/healthy-recipes/?page="
    }

    help = "Popularizes the database with RecipeData fields scraped by beautifulsoup"

    def add_arguments(self, parser):
        parser.add_argument('meal_type',
                            type=str,
                            help='Choose from: breakfast, main_course, dessert')
        parser.add_argument('pages_to_iterate',
                            type=int,
                            help='How many pages to iterate during scraping')

    def handle(self, *args, **kwargs) -> None:
        # process kwargs
        meal_type = kwargs['meal_type']
        how_many = kwargs['pages_to_iterate']

        t = time.time()
        # iterate over all the recipes and gather dish names to avoid duplicating
        dish_names_list = [recipe.name for recipe in RecipeData.objects.all() if meal_type == recipe.meal_type]
        elapsed = time.time() - t
        self.stdout.write(f"Ingredient gathering time: {elapsed} seconds elapsed")

        base_address = self.categories[meal_type]

        for i in range(1, how_many):
            url = urllib.request.urlopen(base_address + str(i))
            soup = bs.BeautifulSoup(url, 'lxml')
            div_search = soup.find_all('div', class_='fixed-recipe-card__info')
            for div in div_search:
                h3s = div.find_all('h3', class_='fixed-recipe-card__h3')
                for h3 in h3s:
                    a = h3.find('a')
                    span = a.find_all('span', class_='fixed-recipe-card__title-link')
                    if span[0].text in dish_names_list:
                        self.stdout.write(f"{span[0].text} already in database")
                        continue
                    else:
                        self.stdout.write(span[0].text)
                        ingredients, image_url = self.get_recipe_ingredients(a['href'])
                        ingredients = parse.parse_ingredients(ingredients)
                        self.add_new_ingredients(ingredients)
                        # add new ingredients to ingredients database
                        for ingred in ingredients:
                            self.stdout.write(ingred)
                        recipe = RecipeData(name=span[0].text,
                                            address=a['href'],
                                            ingredients=ingredients,
                                            meal_type=meal_type,
                                            image_url=image_url)
                        recipe.save()
        self.stdout.write("Recipes saved")

    @staticmethod
    def get_recipe_ingredients(address) -> [list, str]:
        url = urllib.request.urlopen(address)
        soup = bs.BeautifulSoup(url, 'html.parser')
        list_ingredients = json.loads(soup.find('script', type='application/ld+json').string)[1]['recipeIngredient']
        try:
            image_url = json.loads(soup.find('script', type='application/ld+json').string)[1]['image']['url']
        except IndexError:
            image_url = ""
        return list_ingredients, image_url

    @staticmethod
    def add_new_ingredients(new_ingredients: list) -> None:
        # pull gathered ingredients to add new for Tagify suggestions
        db_ingredients = Ingredient.objects.all()
        db_ingredients = [obj.name for obj in db_ingredients]
        for ingredient in new_ingredients:
            if ingredient not in db_ingredients:
                Ingredient(name=ingredient).save()
            else:
                pass
