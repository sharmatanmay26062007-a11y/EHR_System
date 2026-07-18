from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LabReportForm


@login_required
def upload_report(request):
    if request.method == 'POST':
        form = LabReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.patient = request.user.patient_profile
            report.uploaded_by = request.user
            report.save()
            messages.success(request, 'Report uploaded successfully.')
            return redirect('my_reports')
    else:
        form = LabReportForm()

    return render(request, 'reports/upload_report.html', {'form': form})


@login_required
def my_reports(request):
    reports = request.user.patient_profile.lab_reports.all()
    return render(request, 'reports/my_reports.html', {'reports': reports})