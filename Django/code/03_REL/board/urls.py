# board/urls.py
from django.urls import path
from . import views

# <app_name>:<pattern_name>
app_name = 'board'

urlpatterns = [
    # board/create/ => board:create
    path('create/', views.create, name='create'),
    # board/  => board:index
    path('', views.index, name='index'),
    # board/1/ => board:deatil, pk
    path('<int:pk>/', views.detail, name='detail'),
    # board/1/update/ => board:update, pk
    path('<int:pk>/update/', views.update, name='update'),
    # board/1/delete/ => board:delete, pk
    path('<int:pk>/delete/', views.delete, name='delete'),

    # board/1/comments/create
    path('<int:pk>/comments/create/', views.create_comment, name='create_comment'),
    # board/1/comments/1/delete/
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    # board/1/like/
    path('<int:pk>/like/', views.like, name='like'),
]   
