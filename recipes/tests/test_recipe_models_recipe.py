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

    def test_recipe_fields_max_length(self):
        fields = [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
            ('preparation_steps', 500),
        ]


        for field, max_length in fields:
            with self.subTest(field=field, max_length=max_length):
                value = 'A' * (max_length + 0)
                setattr(self.recipe, field, value)
                with self.assertRaises(ValidationError):
                    self.recipe.full_clean() # call validation 