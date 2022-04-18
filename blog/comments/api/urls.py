from django.contrib import admin
from django.urls import path
from .views import CommentListAPIView, CommentDetailAPIVies, CommentCreateAPIView

app_name = 'comments-api'

urlpatterns = [
    path('', CommentListAPIView.as_view(), name = 'all'),
    path('<int:pk>/', CommentDetailAPIVies.as_view(), name = 'thread'),
    path('create/', CommentCreateAPIView.as_view(), name = 'create'),
    
    #path('<int:id>/delete/', views.post_delete),
]