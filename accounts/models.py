from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    ROLE_CHOICES = [
        ("vet", "Veterinário"),
        ("attendant", "Atendente"),
        ("admin", "Administrador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

