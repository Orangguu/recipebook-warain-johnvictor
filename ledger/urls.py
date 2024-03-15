from django.urls import path, include
from django.contrib import admin
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path("recipes/list", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>/detail", RecipeDetailView.as_view(), name="recipe-detail"),
]

app_name = "ledger"
