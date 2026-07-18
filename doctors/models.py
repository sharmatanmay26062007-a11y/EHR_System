from django.conf import settings
from django.db import models


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=150, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    available_days = models.CharField(
        max_length=100, blank=True,
        help_text="e.g. Mon, Wed, Fri"
    )
    available_time = models.CharField(
        max_length=50, blank=True,
        help_text="e.g. 10:00 AM - 4:00 PM"
    )

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username} ({self.specialization})"