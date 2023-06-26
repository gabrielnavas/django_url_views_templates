from django.test import TestCase
from django.urls import reverse, resolve

from recipes import views

class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_by_id_url_is_correct(self):
        recipe_id = 1
        home_url = reverse('recipes:recipe', kwargs={'id': recipe_id})
        self.assertEqual(home_url, f'/recipes/{recipe_id}')

    def test_recipe_by_category_url_is_correct(self):
        category_id = 1
        home_url = reverse('recipes:category', kwargs={'id': category_id})
        self.assertEqual(home_url, f'/recipes/category/{category_id}')

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        category_id = 1
        view = resolve(reverse('recipes:category', kwargs={'id': category_id}))
        self.assertIs(view.func, views.category)

    def test_recipe_by_id_view_function_is_correct(self):
        recipe_id = 1
        view = resolve(reverse('recipes:recipe', kwargs={'id': recipe_id}))
        self.assertIs(view.func, views.recipe)