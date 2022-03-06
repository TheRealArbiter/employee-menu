from rest_framework import serializers
from employee_menu_service.apps.menu import models
class MenuSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = "__all__"