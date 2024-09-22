from django.test import TestCase
from recipes.models import *
from django.contrib.auth.models import User

class IngredientTestCase(TestCase):
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

        self.user = User.objects.create()
        UserIngredient.objects.create(user=self.user, ingredient=self.bread)
        UserIngredient.objects.create(user=self.user, ingredient=self.ham)
        UserIngredient.objects.create(user=self.user, ingredient=self.turkey)
        UserIngredient.objects.create(user=self.user, ingredient=self.cheese)

    def test_user_can_make(self):
        self.assertEqual(self.cheese.user_can_make(self.user), [self.ham_and_cheese_sandwich])
        self.assertEqual(self.bread.user_can_make(self.user).sort(), [self.ham_sandwich, self.turkey_sandwich, self.ham_and_cheese_sandwich].sort())
