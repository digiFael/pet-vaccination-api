from django.db import models
from django.conf import settings
from pets.models import Pet
from vaccines.models import Vaccine


class VaccinationRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine = models.ForeignKey(Vaccine, on_delete=models.PROTECT)

    applied_at = models.DateField()
    dose_number = models.PositiveIntegerField()

    notes = models.TextField(blank=True)

    # Quem registrou/aplicou (funcionário)
    applied_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vaccinations_applied"
    )

    class Meta:
        unique_together = ("pet", "vaccine", "dose_number")

    def __str__(self):
        return f"{self.pet.name} - {self.vaccine.name} (Dose {self.dose_number})"

