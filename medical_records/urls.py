from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:appointment_id>/', views.add_record, name='add_record'),
    path('history/', views.view_history, name='view_history'),
]