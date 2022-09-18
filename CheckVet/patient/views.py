from django.shortcuts import render


def main_patient(request):
    return render(request, "patient/patient.html", {"title": "PATIENT"})

