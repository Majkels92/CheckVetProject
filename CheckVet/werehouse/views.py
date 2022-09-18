from django.shortcuts import render
from django.http import HttpResponse


def main_werehouse(request):
    return render(request, "werehouse/werehouse.html", {"app_title": "WEREHOUSE"})
