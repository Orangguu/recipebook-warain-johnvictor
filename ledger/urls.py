from django.urls import path, include
from django.contrib import admin
from .views import index, recipe_list, recipe_1, recipe_2

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/l', recipe_1, name='recipe_1'),
    path('recipe/2', recipe_2, name='recipe_2')
]

app_name = 'ledger'