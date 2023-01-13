from rest_framework import serializers

from .models import Position, Employees


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'