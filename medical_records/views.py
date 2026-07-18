from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from appointments.models import Appointment
from patient.models import PatientProfile

from .forms import MedicalRecordForm, PrescriptionFormSet


@login_required
def add_record(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, id=appointment_id, doctor=request.user.doctor_profile
    )

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = appointment.patient
            record.doctor = appointment.doctor
            record.appointment = appointment
            record.save()

            formset = PrescriptionFormSet(request.POST, instance=record)
            if formset.is_valid():
                formset.save()

            messages.success(request, 'Medical record added successfully.')
            return redirect('appointment_list')
    else:
        form = MedicalRecordForm()
        formset = PrescriptionFormSet()

    return render(request, 'medical_records/add_record.html', {
        'form': form, 'formset': formset, 'appointment': appointment
    })


@login_required
def view_history(request):
    patient = get_object_or_404(PatientProfile, id=request.user.patient_profile.id)
    records = patient.medical_records.all().prefetch_related('prescriptions')
    return render(request, 'medical_records/history.html', {'records': records})