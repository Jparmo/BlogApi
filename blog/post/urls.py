from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name = 'list'),
    path('<int:id>/', views.post_individual, name = 'detail'),
    path('create/', views.post_create, name='create'),
    path('<int:id>/edit/', views.post_update, name='edit'),
    path('<int:id>/delete/', views.post_delete),
]