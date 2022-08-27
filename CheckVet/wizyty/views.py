from django.shortcuts import render
from django.http import HttpResponse


def main_wizyty(request):
    return render(request, "wizyty/wizyty.html", {"app_title": "WIZYTY"})
