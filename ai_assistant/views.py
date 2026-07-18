from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from medical_records.models import MedicalRecord
from reports.models import LabReport

from .forms import SymptomForm
from .models import ChatHistory
from .services import check_symptoms, explain_medical_text


@login_required
def explain_record(request, record_id):
    """Generate an AI explanation for a medical record's diagnosis/notes."""
    record = get_object_or_404(MedicalRecord, id=record_id, patient=request.user.patient_profile)

    if not record.ai_summary:
        text_to_explain = f"Diagnosis: {record.diagnosis}. Notes: {record.notes}"
        record.ai_summary = explain_medical_text(text_to_explain)
        record.save()

    return redirect('view_history')


@login_required
def explain_report(request, report_id):
    """Generate an AI explanation for a lab report type."""
    report = get_object_or_404(LabReport, id=report_id, patient=request.user.patient_profile)

    if not report.ai_explanation:
        report.ai_explanation = explain_medical_text(f"Lab report type: {report.report_type}")
        report.save()

    return redirect('my_reports')


@login_required
def symptom_checker(request):
    """Chatbot-style symptom checker."""
    history = request.user.patient_profile.chat_history.all()[:10]

    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            result = check_symptoms(symptoms)

            ChatHistory.objects.create(
                patient=request.user.patient_profile,
                user_message=symptoms,
                ai_response=result['causes'],
                urgency_level=result['urgency'],
            )
            return redirect('symptom_checker')
    else:
        form = SymptomForm()

    return render(request, 'ai_assistant/symptom_checker.html', {
        'form': form, 'history': history
    })