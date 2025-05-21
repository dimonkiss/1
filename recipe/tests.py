from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

# Create your tests here.

class RecipeViewsTest(TestCase):
    def setUp(self):
        # Створюємо тестові категорії
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')
        
        # Створюємо тестові рецепти
        self.recipe1 = Recipe.objects.create(title='Recipe 1', category=self.category1)
        self.recipe2 = Recipe.objects.create(title='Recipe 2', category=self.category1)
        self.recipe3 = Recipe.objects.create(title='Recipe 3', category=self.category2)
        self.recipe4 = Recipe.objects.create(title='Recipe 4', category=self.category2)
        self.recipe5 = Recipe.objects.create(title='Recipe 5', category=self.category1)
        self.recipe6 = Recipe.objects.create(title='Recipe 6', category=self.category2)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        self.assertEqual(len(response.context['latest_recipes']), 5)
        self.assertEqual(response.context['latest_recipes'][0], self.recipe6)

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/category_list.html')
        categories = response.context['categories']
        self.assertEqual(len(categories), 2)
        self.assertEqual(categories[0].recipe_count, 3)  # Category 1 has 3 recipes
        self.assertEqual(categories[1].recipe_count, 3)  # Category 2 has 3 recipes
