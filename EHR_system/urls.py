"""
URL configuration for EHR_system project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
   path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('appointments/', include('appointments.urls')),
    path('records/', include('medical_records.urls')),
    path('reports/', include('reports.urls')),
    path('ai/', include('ai_assistant.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)