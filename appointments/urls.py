from django.urls import path

from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('list/', views.appointment_list, name='appointment_list'),
    path('<int:id>/status/<str:new_status>/', views.update_status, name='update_status'),
]