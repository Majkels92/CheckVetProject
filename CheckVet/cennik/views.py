from django.shortcuts import render
from django.http import HttpResponse


def main_cennik(request):
    return render(request, "cennik/cennik.html", {"app_title": "CENNIK"})
