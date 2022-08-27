from django.shortcuts import render
from django.http import HttpResponse


def main_klient(request):
    return render(request, "klient/klient.html", {"app_title": "KLIENCI"})
