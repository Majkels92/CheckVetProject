from django.shortcuts import render
from django.http import HttpResponse


def main_dokumenty(request):
    return render(request, "dokumenty/dokumenty.html", {"app_title": "DOKUMENTY"})