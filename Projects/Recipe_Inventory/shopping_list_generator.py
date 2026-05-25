"""Recipe Inventory and Shopping List Generator

This program uses Python fundamentals to compare pantry stock with recipe needs,
prepare a shopping list, and demonstrate data processing with:
- variables and numeric math
- strings for ingredient labels and user prompts
- tuples for fixed ingredient amounts and units
- dictionaries for recipes and inventory
- lists for recipe selection and final shopping items
- sets to remove duplicate ingredients
- conditionals to determine missing items
- loops to collect user choices and build output
- functions to keep the code organized
"""

from typing import Dict, List, Set, Tuple

Recipe = Dict[str, Tuple[float, str]]
RecipeBook = Dict[str, Recipe]
Pantry = Dict[str, Tuple[float, str]]

RECIPE_BOOK: RecipeBook = {
    "Pasta Salad": {
        "pasta": (200.0, "grams"),
        "tomato": (2.0, "pieces"),
        "olive oil": (2.0, "tablespoons"),
        "salt": (0.5, "teaspoons"),
    },
    "Omelette": {
        "eggs": (3.0, "pieces"),
        "milk": (50.0, "ml"),
        "cheese": (50.0, "grams"),
        "pepper": (0.25, "teaspoons"),
    },
    "Fruit Smoothie": {
        "banana": (1.0, "piece"),
        "yogurt": (150.0, "grams"),
        "honey": (1.0, "tablespoon"),
        "berries": (100.0, "grams"),
    },
}

DEFAULT_PANTRY: Pantry = {
    "pasta": (100.0, "grams"),
    "tomato": (1.0, "pieces"),
    "eggs": (2.0, "pieces"),
    "milk": (200.0, "ml"),
    "cheese": (20.0, "grams"),
}


def select_recipes(recipe_book: RecipeBook) -> List[str]:
    print("Available recipes:")
    for recipe in sorted(recipe_book):
        print(f"- {recipe}")

    selected: List[str] = []
    while True:
        choice = input("Enter a recipe name to add or press Enter to finish: ").strip()
        if not choice:
            break

        normalized = choice.title()
        if normalized in recipe_book:
            selected.append(normalized)
            print(f"Added {normalized}")
        else:
            print(f"Recipe '{choice}' not found. Please choose one from the list.")

    return selected


def build_shopping_list(selected_recipes: List[str], recipe_book: RecipeBook, pantry: Pantry) -> Dict[str, Tuple[float, str]]:
    required: Dict[str, Tuple[float, str]] = {}

    for recipe_name in selected_recipes:
        recipe = recipe_book[recipe_name]
        for ingredient, (amount, unit) in recipe.items():
            if ingredient in required:
                current_amount, current_unit = required[ingredient]
                if current_unit == unit:
                    required[ingredient] = (current_amount + amount, unit)
                else:
                    required[f"{ingredient} ({unit})"] = (amount, unit)
            else:
                required[ingredient] = (amount, unit)

    shopping_list: Dict[str, Tuple[float, str]] = {}
    for ingredient, (needed_amount, unit) in required.items():
        pantry_amount, pantry_unit = pantry.get(ingredient, (0.0, unit))
        if pantry_unit != unit:
            print(f"Note: pantry has {ingredient} in '{pantry_unit}', recipe needs '{unit}'.")
            pantry_amount = 0.0

        if needed_amount > pantry_amount:
            shopping_list[ingredient] = (needed_amount - pantry_amount, unit)

    return shopping_list


def display_shopping_list(shopping_list: Dict[str, Tuple[float, str]], selected_recipes: List[str]) -> None:
    print("\n=== Shopping List ===")
    if not selected_recipes:
        print("No recipes were selected.")
        return

    print(f"Selected recipes: {', '.join(selected_recipes)}")
    if not shopping_list:
        print("Your pantry already contains everything needed.")
        return

    for ingredient, (amount, unit) in sorted(shopping_list.items()):
        print(f"- {ingredient}: {amount:.2f} {unit}")


def run_shopping_list_generator() -> None:
    print("Welcome to the Recipe Inventory and Shopping List Generator")
    print("This tool compares recipe requirements with pantry inventory.")

    selected_recipes = select_recipes(RECIPE_BOOK)
    shopping_list = build_shopping_list(selected_recipes, RECIPE_BOOK, DEFAULT_PANTRY)
    display_shopping_list(shopping_list, selected_recipes)
    print("Thanks for using the recipe inventory tool.")


def main() -> None:
    run_shopping_list_generator()


if __name__ == "__main__":
    main()
