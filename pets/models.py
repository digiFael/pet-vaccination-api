from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    SPECIES_CHOICES = [
        ("dog", "Cachorro"),
        ("cat", "Gato"),
        ("other", "Outro"),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")

    def __str__(self):
        return f"{self.name} ({self.species})"