from django.shortcuts import render
from django.http import HttpResponse


def main_appointment(request):
    return render(request, "appointment/appointment.html", {"app_title": "APPOINTMENT"})
