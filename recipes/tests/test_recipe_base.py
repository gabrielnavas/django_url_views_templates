from django.test import TestCase

from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='any_fake_category') -> Category:
        return Category.objects.create(name=name)
    
    def make_author(
        self, 
        username='any_username', 
        email='any_email@email.com', 
        password='any_password',
        first_name='any_name',
        last_name='any_last_name'
    ):
        return User.objects.create_user(
                username=username, 
                email=email, 
                password=password,
                first_name=first_name,
                last_name=last_name
        )
    
    def make_recipe(
        self,
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
        category_data=None,
        author_data=None
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
        )