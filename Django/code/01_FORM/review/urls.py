from django.urls import path
from . import views


urlpatterns = [
    # /review/
    path('', views.index),
    
]
