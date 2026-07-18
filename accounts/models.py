from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        PATIENT = 'patient', 'Patient'
        DOCTOR = 'doctor', 'Doctor'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(max_length=10, choices=Role.choices)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} - {self.role}"

    @property
    def is_patient(self):
        return self.role == self.Role.PATIENT

    @property
    def is_doctor(self):
        return self.role == self.Role.DOCTOR