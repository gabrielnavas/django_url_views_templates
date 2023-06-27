from django.urls import reverse, resolve

from recipes import views

from recipes.tests.test_recipe_base import RecipeTestBase

class RecipeCategoryViewsTest(RecipeTestBase):
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

    def test_recipe_category_template_dont_load_recipe_not_published(self):
        """Test recipe is_published False dont show"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:category', kwargs={'id': recipe.category.id}))
        HTTP_CODE_NOT_FOUND = 404
        self.assertEqual(response.status_code, HTTP_CODE_NOT_FOUND)
