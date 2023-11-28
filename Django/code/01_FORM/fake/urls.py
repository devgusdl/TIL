from django.urls import path
from . import views

urlpatterns = [
    # /fake/
    path('', views.index),
]
