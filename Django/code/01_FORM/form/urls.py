from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('fake/', include('fake.urls')),
    path('user_input/', include('user_input.urls')),
]
