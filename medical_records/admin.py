from django.contrib import admin

from .models import MedicalRecord, Prescription


class PrescriptionInline(admin.TabularInline):
    model = Prescription
    extra = 1


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diagnosis', 'date')
    list_filter = ('date',)
    search_fields = ('patient__user__username', 'diagnosis')
    inlines = [PrescriptionInline]