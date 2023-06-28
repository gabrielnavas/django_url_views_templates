from django.core.exceptions import ValidationError

from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeModelsTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 66

        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # call validation 