from django.test import TestCase
from django.urls import reverse, resolve

from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User

class RecipeViewsTest(TestCase):
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
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here.</h1>', 
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_correct_context_recipes(self):
        category = Category.objects.create(name='any_fake_category')
        author = User.objects.create_user(
            username='any_username', 
            email='any_email@email.com', 
            password='any_password',
            first_name='any_name',
            last_name='any_last_name'
        )
        Recipe.objects.create(
            title = 'any_title',
            description = 'any_description',
            slug = 'any-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutes',
            servings = 5,
            servings_unit = 'Unit',
            preparation_steps = 'any_steps',
            preparation_steps_is_html = False,
            is_published = True,
            category=category,
            author=author,
        )
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
        self.assertEqual(response_recipe.category.name, category.name)
        self.assertEqual(response_recipe.author.username, author.username)

    def test_recipe_home_template_loads_correct_content_recipes(self):
        category = Category.objects.create(name='any_fake_category')
        author = User.objects.create_user(
            username='any_username', 
            email='any_email@email.com', 
            password='any_password',
            first_name='any_name',
            last_name='any_last_name'
        )
        Recipe.objects.create(
            title = 'any_title',
            description = 'any_description',
            slug = 'any-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutes',
            servings = 5,
            servings_unit = 'Unit',
            preparation_steps = 'any_steps',
            preparation_steps_is_html = False,
            is_published = True,
            category=category,
            author=author,
        )
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