from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.main_documents, name='documents_home'),
]