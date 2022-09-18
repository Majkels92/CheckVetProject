from django.shortcuts import render
from django.http import HttpResponse


def main_documents(request):
    return render(request, "documents/documents.html", {"app_title": "DOCUMENTS"})