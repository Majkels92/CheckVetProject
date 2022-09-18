from django.shortcuts import render
from django.http import HttpResponse


def main_client(request):
    return render(request, "client/client.html", {"app_title": "CLIENT"})
