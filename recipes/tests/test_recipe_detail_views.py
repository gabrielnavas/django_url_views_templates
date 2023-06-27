from django.urls import reverse, resolve

from recipes import views

from recipes.tests.test_recipe_base import RecipeTestBase

class RecipeDetailViewsTest(RecipeTestBase):
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

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """Test recipe is_published False dont show"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
        HTTP_CODE_NOT_FOUND = 404
        self.assertEqual(response.status_code, HTTP_CODE_NOT_FOUND)
