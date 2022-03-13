from rest_framework import serializers
from employee_menu_service.apps.meals import models


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meals
        fields = "__all__"