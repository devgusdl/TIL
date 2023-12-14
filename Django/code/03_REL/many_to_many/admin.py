from django.contrib import admin
from .models import Actor, Movie

admin.site.register(Actor)
admin.site.register(Movie)

# python manage.py createsuperuser