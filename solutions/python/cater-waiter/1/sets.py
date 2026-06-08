"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    return (
        f"{drink_name} Cocktail"
        if set(drink_ingredients) & ALCOHOLS
        else f"{drink_name} Mocktail"
    )


def categorize_dish(dish_name, dish_ingredients):
    categories = [
        ("VEGAN", VEGAN),
        ("VEGETARIAN", VEGETARIAN),
        ("PALEO", PALEO),
        ("KETO", KETO),
        ("OMNIVORE", OMNIVORE),
    ]

    for name, category in categories:
        if dish_ingredients.issubset(category):
            return f"{dish_name}: {name}"


def tag_special_ingredients(dish):
    sep = set()

    for item in dish[1]:
        if item in SPECIAL_INGREDIENTS:
            sep.add(item)

    return (dish[0], sep)


def compile_ingredients(dishes):
    return set().union(*dishes)

def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    return set().union(*dishes) - intersection
