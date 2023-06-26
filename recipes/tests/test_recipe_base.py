from django.test import TestCase

from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
            category = self.make_recipe()
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
            return super().setUp()

    def make_recipe(self, name='any_fake_category') -> Category:
        return Category.objects.create(name=name)
    