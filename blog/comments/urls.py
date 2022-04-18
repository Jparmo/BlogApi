from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.comment_thread, name = 'thread'),
    #path('<int:id>/delete/', views.post_delete),
]