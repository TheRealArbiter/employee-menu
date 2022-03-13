from django.contrib import admin
from .models import Meals

@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):  
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ('name', )
