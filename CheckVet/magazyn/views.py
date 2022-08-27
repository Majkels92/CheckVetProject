from django.shortcuts import render
from django.http import HttpResponse


def main_magazyn(request):
    return render(request, "magazyn/magazyn.html", {"app_title": "MAGAZYN"})
