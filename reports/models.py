from django.conf import settings
from django.db import models

from patient.models import PatientProfile


class LabReport(models.Model):
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name='lab_reports'
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    file = models.FileField(upload_to='lab_reports/%Y/%m/')
    report_type = models.CharField(max_length=100, help_text="e.g. Blood Test, X-Ray")
    ai_explanation = models.TextField(blank=True, help_text="Patient-friendly AI explanation")
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_uploaded']

    def __str__(self):
        return f"{self.report_type} - {self.patient} ({self.date_uploaded.date()})"