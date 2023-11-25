# Master URL
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/first_app/
    path('first_app/', include('first_app.urls')),

    # second_app 의 모든 패턴은 'second_app/' 으로 시작
    path('second_app/', include('second_app.urls')),
]