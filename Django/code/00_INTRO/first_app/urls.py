# first_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # /first_app/hello/
    path('hello/', views.hello),
    # /first_app/bye/
    path('bye/', views.bye),
    # /first_app/lotto/
    path('lotto/', views.lotto),
    # /first_app/lunch/
    path('lunch/', views.lunch), 
]
