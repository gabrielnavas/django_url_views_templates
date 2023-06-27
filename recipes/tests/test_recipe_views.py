from unittest import skip

from django.urls import reverse, resolve

from recipes import views

from recipes.tests.test_recipe_base import RecipeTestBase

class RecipeViewsTest(RecipeTestBase):
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
        self.make_recipe()
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

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            '<h1>No recipes found here.</h1>', 
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_correct_content_recipes(self):
        self.make_recipe()
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

    def test_recipe_category_template_loads_recipes(self):
        title_expected = 'This is a category test'
        recipe = self.make_recipe(title=title_expected)

        response = self.client.get(reverse('recipes:category', args=(recipe.category.id, )))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn(title_expected, content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_detail_view_function_is_correct(self):
        recipe_id = 1
        view = resolve(reverse('recipes:recipe', kwargs={'id': recipe_id}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_404_if_no_recipes_found(self):
        recipe_fake_id = 1000
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe_fake_id}))
        HTTP_CODE_NOT_FOUND = 404
        self.assertEqual(response.status_code, HTTP_CODE_NOT_FOUND) 

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        title_expected = 'This is a detail page - It load one recipe'
        recipe = self.make_recipe(title=title_expected)

        response = self.client.get(reverse('recipes:recipe', kwargs={ 'id': recipe.id }))
        content = response.content.decode('utf-8')

        self.assertIn(title_expected, content)

