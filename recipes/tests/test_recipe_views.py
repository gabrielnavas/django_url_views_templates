from django.test import TestCase
from django.urls import reverse, resolve

from recipes import views

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

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        STATUS_OK = 200
        self.assertEqual(response.status_code, STATUS_OK)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_norecipes_found_if_norecipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here.</h1>', 
            response.content.decode('utf-8')
        )

    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        category_fake_id = 1000
        response = self.client.get(reverse('recipes:category', kwargs={'id': category_fake_id}))
        HTTP_CODE_NOT_FOUND = 404
        self.assertEqual(response.status_code, HTTP_CODE_NOT_FOUND) 