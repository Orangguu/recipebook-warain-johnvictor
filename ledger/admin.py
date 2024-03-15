from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Recipe, RecipeIngredient, Ingredient, Profile


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        RecipeIngredientInLine,
    ]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_deleted = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInLine,
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
# Register your models here.
