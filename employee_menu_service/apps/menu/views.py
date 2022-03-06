from django.shortcuts import render
from rest_framework import viewsets, status
from employee_menu_service.apps.menu.models import Menu
from employee_menu_service.apps.menu.serializers import MenuSeriaizer
# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSeriaizer
    queryset = Menu.objects.all()
    filterset_fields = ('name',)