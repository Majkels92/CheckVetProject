from django.shortcuts import render


def main_pacjent(request):
    return render(request, "pacjent/pacjent.html", {"title": "PACJENCI"})

