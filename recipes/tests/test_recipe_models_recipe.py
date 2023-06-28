from django.core.exceptions import ValidationError
from parameterized import parameterized

from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeModelsTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 66

        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # call validation 

    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field: str, max_length: int):
        value = 'A' * (max_length + 1)
        setattr(self.recipe, field, value)
        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # call validation 