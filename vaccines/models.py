from django.db import models


class Vaccine(models.Model):
    SPECIES_TARGET = [
        ("dog", "Cachorro"),
        ("cat", "Gato"),
        ("both", "Ambos"),
    ]

    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    species_target = models.CharField(max_length=20, choices=SPECIES_TARGET)

    doses_required = models.PositiveIntegerField(default=1)
    days_between_doses = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
