from django.urls import path
from . import views

urlpatterns = [
    # second_app/fibo/
    path('fibo/', views.fibo),
    
    # second_app/is_xmas/
    path('is_xmas/', views.is_xmas),
]
