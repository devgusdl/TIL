from django.urls import path
from . import views

urlpatterns = [
    # util/
    path('', views.index),
    # util/time/
    path('time/', views.time),
    # util/lotto_in/
    path('lotto_in/', views.lotto_in),
    # util/lotto_out/
    path('lotto_out/', views.lotto_out),
]
