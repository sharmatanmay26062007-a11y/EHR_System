from django.urls import path

from . import views

urlpatterns = [
    path('explain-record/<int:record_id>/', views.explain_record, name='explain_record'),
    path('explain-report/<int:report_id>/', views.explain_report, name='explain_report'),
    path('symptom-checker/', views.symptom_checker, name='symptom_checker'),
]