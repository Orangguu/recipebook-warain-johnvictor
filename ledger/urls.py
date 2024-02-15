from django.urls import path, include
from django.contrib import admin
from .views import recipe_list, recipe_2, recipe_1

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/1', recipe_1, name='recipe_1'),
    path('recipe/2', recipe_2, name='recipe_2')
]

app_name = 'ledger'