from django.contrib import admin

# Register your models here.
# cookbook/ingredients/admin.py
from cookbook.ingredients.models import Category, Ingredient

admin.site.register(Category)
admin.site.register(Ingredient)
