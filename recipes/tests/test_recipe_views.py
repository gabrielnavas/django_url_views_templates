from django.test import TestCase
from django.urls import reverse, resolve

from recipes import views
from recipes.models import Recipe

from recipes.tests.test_recipe_base import RecipeTestBase

class RecipeViewsTest(RecipeTestBase):
    def tearDown(self) -> None:
        return super().tearDown()

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        STATUS_OK = 200
        self.assertEqual(response.status_code, STATUS_OK)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_norecipes_found_if_norecipes(self):
        recipe_id_fake_created = 1
        Recipe.objects.get(id=recipe_id_fake_created).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here.</h1>', 
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_correct_context_recipes(self):
        
        response = self.client.get(reverse('recipes:home'))

        response_recipes = response.context['recipes']
        response_recipe = response.context['recipes'].first()
        recipes_found_length = 1        
        self.assertEqual(len(response_recipes), recipes_found_length)
        self.assertEqual(response_recipe.title, 'any_title')
        self.assertEqual(response_recipe.description, 'any_description')
        self.assertEqual(response_recipe.slug, 'any-slug')
        self.assertEqual(response_recipe.preparation_time, 10)
        self.assertEqual(response_recipe.preparation_time_unit, 'Minutes')
        self.assertEqual(response_recipe.servings, 5)
        self.assertEqual(response_recipe.servings_unit, 'Unit')
        self.assertEqual(response_recipe.preparation_steps, 'any_steps')
        self.assertEqual(response_recipe.preparation_steps_is_html, False)
        self.assertEqual(response_recipe.is_published, True)

    def test_recipe_home_template_loads_correct_content_recipes(self):
        response = self.client.get(reverse('recipes:home'))

        content = response.content.decode('utf-8')
        self.assertIn('any_title', content)
        self.assertIn('any_description', content)
        self.assertIn('10 Minutes', content)
        self.assertIn('5 Unit', content)
        

    def test_recipe_category_view_function_is_correct(self):
        category_id = 1
        view = resolve(reverse('recipes:category', kwargs={'id': category_id}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        category_fake_id = 1000
        response = self.client.get(reverse('recipes:category', kwargs={'id': category_fake_id}))
        HTTP_CODE_NOT_FOUND = 404
        self.assertEqual(response.status_code, HTTP_CODE_NOT_FOUND) 

    def test_recipe_detail_view_function_is_correct(self):
        recipe_id = 1
        view = resolve(reverse('recipes:recipe', kwargs={'id': recipe_id}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_404_if_no_recipes_found(self):
        recipe_fake_id = 1000
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe_fake_id}))
        HTTP_CODE_NOT_FOUND = 404
        self.assertEqual(response.status_code, HTTP_CODE_NOT_FOUND) 