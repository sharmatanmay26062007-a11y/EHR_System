from django.db import models

from patient.models import PatientProfile


class ChatHistory(models.Model):
    class Urgency(models.TextChoices):
        MILD = 'mild', 'Mild'
        MODERATE = 'moderate', 'Moderate'
        URGENT = 'urgent', 'Urgent - See a doctor'

    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, related_name='chat_history'
    )
    user_message = models.TextField(help_text="Symptoms described by the patient")
    ai_response = models.TextField(help_text="AI's suggested possible causes")
    urgency_level = models.CharField(max_length=10, choices=Urgency.choices, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Chat histories'

    def __str__(self):
        return f"{self.patient} - {self.created_at.strftime('%d %b %Y')}"