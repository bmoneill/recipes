from django.test import TestCase
from recipes.models import *

class RecipeTestCase(TestCase):
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


    def test_user_can_make(self):
        self.user = RecipesUser.objects.create()
        UserIngredient.objects.create(user=self.user, ingredient=self.bread)
        UserIngredient.objects.create(user=self.user, ingredient=self.ham)
        UserIngredient.objects.create(user=self.user, ingredient=self.cheese)

        self.assertEqual(self.ham_and_cheese_sandwich.user_can_make(self.user), True)
        self.assertEqual(self.turkey_sandwich.user_can_make(self.user), False)

    def test_user_can_almost_make(self):
        self.user = RecipesUser.objects.create()
        UserIngredient.objects.create(user=self.user, ingredient=self.bread)
        UserIngredient.objects.create(user=self.user, ingredient=self.ham)
        UserIngredient.objects.create(user=self.user, ingredient=self.cheese)

        self.assertEqual(self.ham_and_cheese_sandwich.user_can_almost_make(self.user, 1), True)
        self.assertEqual(self.turkey_sandwich.user_can_almost_make(self.user, 1), True)
        self.assertEqual(self.turkey_sandwich.user_can_almost_make(self.user, 0), False)
        self.assertEqual(self.turkey_and_cheese_sandwich.user_can_almost_make(self.user, 2), True)
