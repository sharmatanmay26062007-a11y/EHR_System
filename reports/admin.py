from django.contrib import admin

from .models import LabReport


@admin.register(LabReport)
class LabReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'report_type', 'uploaded_by', 'date_uploaded')
    list_filter = ('report_type',)