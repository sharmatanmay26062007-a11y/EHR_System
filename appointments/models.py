from django.db import models

from doctors.models import DoctorProfile
from patient.models import PatientProfile


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name='appointments'
    )
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name='appointments'
    )
    date = models.DateField()
    time_slot = models.CharField(max_length=20, help_text="e.g. 11:00 AM")
    reason = models.CharField(max_length=255, blank=True, help_text="Brief reason for visit")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'time_slot']

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date}"