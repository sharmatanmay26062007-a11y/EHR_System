from django.conf import settings
from django.db import models


class PatientProfile(models.Model):
    class BloodGroup(models.TextChoices):
        A_POS = 'A+', 'A+'
        A_NEG = 'A-', 'A-'
        B_POS = 'B+', 'B+'
        B_NEG = 'B-', 'B-'
        O_POS = 'O+', 'O+'
        O_NEG = 'O-', 'O-'
        AB_POS = 'AB+', 'AB+'
        AB_NEG = 'AB-', 'AB-'

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True)
    blood_group = models.CharField(max_length=3, choices=BloodGroup.choices, blank=True)
    address = models.TextField(blank=True)
    allergies = models.TextField(blank=True, help_text="Comma separated, e.g. Penicillin, Peanuts")
    emergency_contact = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}'s profile"