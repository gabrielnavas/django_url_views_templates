from django.test import TestCase
from django.urls import reverse


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
