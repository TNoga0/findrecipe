import re

ingredients_cleanup = [
    # measurement

    'teaspoon',
    'tsp',
    'teaspoons',
    'tsps',
    'tablespoon',
    'tablespoons',
    'tbsp',
    'tbsps',
    'cup',
    'cups',
    'pinch',
    'pinches',
    'slice',
    'slices',
    'pound',
    'pounds',
    'lbs',
    'kilos',
    'kilograms',
    'kilogram',
    'kg',
    'kgs',
    'oz',
    'inch',
    'inches',
    'ounce',
    'ounces',
    'small',
    'medium',
    'large',
    'dash',
    'sprinkle',
    'can',
    'cans',
    'bottle',
    'bottles',
    'litre',
    'liters',
    'litres',
    'container',
    'containers',
    'carton',
    'cartons',
    'thin',
    'thick',
    'very',
    'little',
    'small',
    'big',
    'package',
    'packages',
    'clove',
    'cloves',
    'frozen',
    'warm',
    'cold',
    'hot',
    'optional',
    '(optional)',
    'packed',
    'baked',
    'unbaked',
    'quart',
    'canned',
    'finely',
    'your',
    'favorite',
    'favourite',
    'fluid',
    'root',
    'or',
    'jar',
    'deep',
    'dish',
    'fresh',
    'grinds',
    'loaf',
    'loaves',

    # preparation

    'melted',
    'shredded',
    'processed',
    'ground',
    'minced',
    'diced',
    'roasted',
    'cooked',
    'sifted',
    'separated',
    'beaten',
    'drained',
    'thawed',
    'peeled',
    'dried',
    'grated',
    'chopped',
    'sharp',
    'mild',
    'to',
    'taste',
    'refrigerated',
    'lean',
    'crushed',
    'prepared',
    'seasoned',
    'italian-style',
    'flat-leaf',
    'condensed',

    # some characters to be deleted as deemed unnecessary:

    ':',
    ';',
    '.',
    ',',

    # garbage words

    'such',
    'as',
    'serving',

]


# below a dict that says what to do with specific pairs of ingredients, e.g. salt and pepper
# should be represented as separate ingredients
ingredients_to_be_swapped = {
    'salt and pepper': ['salt', 'pepper'],
    'pepper and salt': ['salt', 'pepper'],
    'herb and garlic feta': ["feta"],
}


def parse_ingredients(ingredients: list):
    for i, ingredient in enumerate(ingredients):
        append_keys = []
        ingredient = re.sub("[\(\[].*?[\)\]]", "", ingredient)
        # remove those usual-occurring stuff like "(...), melted" or "(...), shredded
        words = ingredient.split(", ")[0].split(" ")
        # use list comprehension to eliminate numbers, fractions and words that are not ingredients
        if 'ground' in words and words[words.index('ground') + 1] == 'cloves':
            ingredients[i] = 'ground cloves'
            continue
        words = [word.lower() for word in words if all([word not in ingredients_cleanup,
                                                word.isnumeric() is False,
                                                u'\u2009' not in word,
                                                word,  # if it is not an empty string
                                                '(' not in word,
                                                ')' not in word])]

        # TODO maybe change the index from 1 to -1 to improve performance
        if " ".join(words) == '' and ingredient.split(",")[1].split(" "):
            words = ingredient.split(",")[1].split(" ")
            words.remove("")
            # use list comprehension to eliminate numbers, fractions and words that are not ingredients
            if 'ground' in words and words[words.index('ground') + 1] == 'cloves':
                ingredients[i] = 'ground cloves'
                continue
            words = [word.lower() for word in words if all([word not in ingredients_cleanup,
                                                    word.isnumeric() is False,
                                                    u'\u2009' not in word,
                                                    word,  # if it is not an empty string
                                                    '(' not in word,
                                                    ')' not in word])]

        # remove all the dangling '-' characters
        try:
            words.remove('-')
        except Exception:
            pass

        for key, values in ingredients_to_be_swapped.items():
            if key in " ".join(words):
                append_keys.append(key)
            else:
                ingredients[i] = " ".join(words)

    ingredients = list(dict.fromkeys(ingredients))

    if 'append_keys' not in locals():
        append_keys = []

    for key in append_keys:
        for value in ingredients_to_be_swapped[key]:
            ingredients.append(value)
        ingredients.remove(key)

    return ingredients
