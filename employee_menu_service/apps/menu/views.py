from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import viewsets, status
from employee_menu_service.apps.menu.models import Menu
from employee_menu_service.apps.menu.serializers import MenuSeriaizer
from employee_menu_service.apps.mixins import PaginationHandlerMixin

class PaginationClass(LimitOffsetPagination):
    default_limit = 10
class MenuViewSet(viewsets.ModelViewSet, PaginationHandlerMixin):
    pagination_class = PaginationClass
    serializer_class = MenuSeriaizer
    queryset = Menu.objects.all()
    filterset_fields = ('name',)
    
    
    def get(self, request, format=None, *args, **kwargs):
        """ Get all list """
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_paginated_response(
                self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(self.get_queryset(), many=True).data
        return Response(serializer.data, status=status.HTTP_200_OK)
