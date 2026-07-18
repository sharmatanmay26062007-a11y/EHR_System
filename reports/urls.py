from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.upload_report, name='upload_report'),
    path('my/', views.my_reports, name='my_reports'),
]