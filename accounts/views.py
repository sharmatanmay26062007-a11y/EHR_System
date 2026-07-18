from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from doctors.models import DoctorProfile
from patient.models import PatientProfile

from .forms import LoginForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            if user.role == user.Role.PATIENT:
                PatientProfile.objects.create(user=user)
            elif user.role == user.Role.DOCTOR:
                DoctorProfile.objects.create(user=user)

            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect_by_role(user)
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def redirect_by_role(user):
    if user.role == user.Role.PATIENT:
        return redirect('patient_dashboard')
    elif user.role == user.Role.DOCTOR:
        return redirect('doctor_dashboard')
    else:
        return redirect('admin_dashboard')