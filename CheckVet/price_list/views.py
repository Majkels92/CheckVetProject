from django.shortcuts import render
from django.http import HttpResponse


def main_price_list(request):
    return render(request, "price_list/price_list.html", {"app_title": "PRICE_LIST"})
