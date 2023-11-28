from django.urls import path
from . import views

urlpatterns = [
    path('lotto_in/', views.lotto_in),
    path('lotto_out/', views.lotto_out),
]
