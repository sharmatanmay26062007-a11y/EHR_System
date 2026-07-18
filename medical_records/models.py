from django.db import models

from appointments.models import Appointment
from doctors.models import DoctorProfile
from patient.models import PatientProfile


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name='medical_records'
    )
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name='medical_records'
    )
    appointment = models.ForeignKey(
        Appointment, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='medical_record'
    )
    diagnosis = models.CharField(max_length=255)
    notes = models.TextField(help_text="Doctor's raw consultation notes")
    ai_summary = models.TextField(blank=True, help_text="AI-generated structured summary")
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.diagnosis} - {self.patient} ({self.date})"


class Prescription(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='prescriptions'
    )
    medicine_name = models.CharField(max_length=150)
    dosage = models.CharField(max_length=50, help_text="e.g. 500mg")
    duration = models.CharField(max_length=50, help_text="e.g. 5 days")
    instructions = models.CharField(max_length=255, blank=True, help_text="e.g. After meals")

    def __str__(self):
        return f"{self.medicine_name} ({self.dosage}) - {self.medical_record.patient}"