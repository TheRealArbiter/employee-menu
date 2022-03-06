from rest_framework import serializers

class MenuSeriaizer(serializers.Serializer):
    persons = serializers.ListField(required=False)