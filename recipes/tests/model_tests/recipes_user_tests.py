from django.test import TestCase
from recipes.models import *

class RecipesUserTestCase(TestCase):
    def setUp(self):
        self.bread = Ingredient.objects.create(name="Bread")
        self.peanut_butter = Ingredient.objects.create(name="Peanut Butter")
        self.jelly = Ingredient.objects.create(name="Jelly")
        self.ham = Ingredient.objects.create(name="Ham")
        self.turkey = Ingredient.objects.create(name="Turkey")
        self.cheese = Ingredient.objects.create(name="Cheese")

        self.pbj = Recipe.objects.create(name="PB&J")
        RecipeIngredient.objects.create(recipe=self.pbj, ingredient=self.bread)
        RecipeIngredient.objects.create(recipe=self.pbj, ingredient=self.peanut_butter)
        RecipeIngredient.objects.create(recipe=self.pbj, ingredient=self.jelly)

        self.ham_sandwich = Recipe.objects.create(name="Ham Sandwich")
        RecipeIngredient.objects.create(recipe=self.ham_sandwich, ingredient=self.bread)
        RecipeIngredient.objects.create(recipe=self.ham_sandwich, ingredient=self.ham)

        self.ham_and_cheese_sandwich = Recipe.objects.create(name="Ham and Cheese Sandwich")
        RecipeIngredient.objects.create(recipe=self.ham_and_cheese_sandwich, ingredient=self.bread)
        RecipeIngredient.objects.create(recipe=self.ham_and_cheese_sandwich, ingredient=self.ham)
        RecipeIngredient.objects.create(recipe=self.ham_and_cheese_sandwich, ingredient=self.cheese)

        self.turkey_sandwich = Recipe.objects.create(name="Turkey Sandwich")
        RecipeIngredient.objects.create(recipe=self.turkey_sandwich, ingredient=self.bread)
        RecipeIngredient.objects.create(recipe=self.turkey_sandwich, ingredient=self.turkey)

        self.turkey_and_cheese_sandwich = Recipe.objects.create(name="Turkey and Cheese Sandwich")
        RecipeIngredient.objects.create(recipe=self.turkey_and_cheese_sandwich, ingredient=self.bread)
        RecipeIngredient.objects.create(recipe=self.turkey_and_cheese_sandwich, ingredient=self.turkey)
        RecipeIngredient.objects.create(recipe=self.turkey_and_cheese_sandwich, ingredient=self.cheese)

    def test_available_recipes(self):
        self.user = RecipesUser.objects.create()
        UserIngredient.objects.create(user=self.user, ingredient=self.bread)
        UserIngredient.objects.create(user=self.user, ingredient=self.ham)
        UserIngredient.objects.create(user=self.user, ingredient=self.cheese)

        self.assertEqual(self.user.available_recipes().sort(), [self.ham_sandwich, self.ham_and_cheese_sandwich].sort())

    def test_has_ingredient(self):
        self.user = RecipesUser.objects.create()
        UserIngredient.objects.create(user=self.user, ingredient=self.bread)
        UserIngredient.objects.create(user=self.user, ingredient=self.ham)
        UserIngredient.objects.create(user=self.user, ingredient=self.cheese)

        self.assertEqual(self.user.has_ingredient(self.ham), True)
        self.assertEqual(self.user.has_ingredient(self.turkey), False)

    def test_num_missing_ingredients(self):
        self.user = RecipesUser.objects.create()
        UserIngredient.objects.create(user=self.user, ingredient=self.bread)
        UserIngredient.objects.create(user=self.user, ingredient=self.ham)
        UserIngredient.objects.create(user=self.user, ingredient=self.cheese)

        self.assertEqual(self.user.num_missing_ingredients(self.pbj), 2)
        self.assertEqual(self.user.num_missing_ingredients(self.turkey_sandwich), 1)
        self.assertEqual(self.user.num_missing_ingredients(self.ham_and_cheese_sandwich), 0)

    def test_unavailable_recipes(self):
        self.user = RecipesUser.objects.create()
        UserIngredient.objects.create(user=self.user, ingredient=self.bread)
        UserIngredient.objects.create(user=self.user, ingredient=self.ham)
        UserIngredient.objects.create(user=self.user, ingredient=self.cheese)

        self.assertEqual(self.user.unavailable_recipes().sort(), [self.pbj, self.turkey_sandwich, self.turkey_and_cheese_sandwich].sort())
