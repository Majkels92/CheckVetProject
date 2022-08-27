from django.shortcuts import render


def main_start(request):
    return render(request, "start/start.html", {"app_title": "START"})
