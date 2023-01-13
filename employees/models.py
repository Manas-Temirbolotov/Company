from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    patronymic = models.CharField(max_length=20, null=True, blank=True)


class Position(models.Model):
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.position


class Employees(models.Model):
    fullname = models.CharField(max_length=50)
    date_birth = models.DateField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.fullname
