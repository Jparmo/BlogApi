from django.contrib import admin
from django.urls import path
from .views import PostListAPIView, PostDetailAPIVies, PostUpdateAPIVies, PostDeleteAPIVies, PostCreateAPIVies

app_name = 'post-api'
urlpatterns = [
    path('', PostListAPIView.as_view(), name = 'list'),
    path('<int:pk>/', PostDetailAPIVies.as_view(), name = 'detail'),
    path('create/', PostCreateAPIVies.as_view(), name='create'),
    path('<int:pk>/edit/', PostUpdateAPIVies.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteAPIVies.as_view(), name='delete'),
]