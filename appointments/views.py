from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AppointmentForm
from .models import Appointment


@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient_profile
            appointment.save()
            messages.success(request, 'Appointment booked successfully.')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form})


@login_required
def appointment_list(request):
    if request.user.is_doctor:
        appointments = request.user.doctor_profile.appointments.all()
    else:
        appointments = request.user.patient_profile.appointments.all()

    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})


@login_required
def update_status(request, id, new_status):
    appointment = get_object_or_404(Appointment, id=id, doctor=request.user.doctor_profile)
    appointment.status = new_status
    appointment.save()
    messages.success(request, f'Appointment marked as {new_status}.')
    return redirect('appointment_list')