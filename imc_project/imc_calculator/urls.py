from django.urls import path
from .views import calcular_imc

urlpatterns = [
    path('', calcular_imc, name='calcular_imc'),
]