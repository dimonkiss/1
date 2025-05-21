from django.shortcuts import render
from .models import Recipe, Category
from django.db import models

def main(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'recipe/main.html', {'latest_recipes': latest_recipes})

def category_list(request):
    categories = Category.objects.annotate(recipe_count=models.Count('recipe'))
    return render(request, 'recipe/category_list.html', {'categories': categories})
