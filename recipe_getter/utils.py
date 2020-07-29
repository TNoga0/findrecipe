def check_contents_with_ingredients(recipe, contents):
    recipe_urls_to_return = []
    check = all(item in contents for item in recipe.ingredients)
    if check:
        recipe_urls_to_return.append(recipe.address)