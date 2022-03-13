from rest_framework import serializers
from employee_menu_service.apps.employee import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"