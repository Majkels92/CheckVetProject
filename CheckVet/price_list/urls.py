from django.urls import path
from . import views

urlpatterns = [
    path('price_list/', views.main_price_list, name='price_list_home'),
]