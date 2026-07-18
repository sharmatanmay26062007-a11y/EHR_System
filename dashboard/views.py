from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def patient_dashboard(request):
    profile = request.user.patient_profile
    appointments = profile.appointments.all()[:5]
    records = profile.medical_records.all()[:5]

    context = {
        'profile': profile,
        'appointments': appointments,
        'records': records,
    }
    return render(request, 'dashboard/patient_dashboard.html', context)


@login_required
def doctor_dashboard(request):
    profile = request.user.doctor_profile
    appointments = profile.appointments.all()[:5]

    context = {
        'profile': profile,
        'appointments': appointments,
    }
    return render(request, 'dashboard/doctor_dashboard.html', context)


@login_required
def admin_dashboard(request):
    from accounts.models import CustomUser
    context = {
        'total_patients': CustomUser.objects.filter(role='patient').count(),
        'total_doctors': CustomUser.objects.filter(role='doctor').count(),
    }
    return render(request, 'dashboard/admin_dashboard.html', context)