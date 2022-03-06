from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):  
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ('name', )
