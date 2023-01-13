from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Position, Employees

from .serializers import PositionSerializer, EmployeesSerializer
from .permissions import IsAuthenticatedPermission


class PositionViewSet(viewsets.ModelViewSet):
    """
    API для создания должности
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticatedPermission,]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['position', 'department']
    ordering_fields = ['position', 'department']


class EmployeesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticatedPermission]
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['fullname', 'salary']
    ordering_fields = ['salary',]

    def get_queryset(self):
        super().get_queryset().filter(employees_id=self.kwargs.get('employees_id'))

    def perform_create(self, serializer):
        serializer.save(
            employees_id = self.kwargs.get('employees_id'),
            profile = self.request.user
        )


class EmployeesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticatedPermission,]

    def get_queryset(self):
        return super().get_queryset().filter(employees_id=self.kwargs.get('employees_id'))