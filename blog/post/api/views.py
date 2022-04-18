from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from post.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer
from django.db.models import Q 
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    #query title and content using rest framework
    filter_b = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    
    def get_queryset(self, *args, **kwargs):
        #queryset =  super(PostListAPIView, self).get_queryset(*args,**kwargs)
        queryset = Post.objects.all()
        query = self.request.GET.get("q")
        # query title and content using django
        if query:
            queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
            ).distinct()
        return queryset
    
class PostDetailAPIVies(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'id'
    
class PostUpdateAPIVies(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    
class PostDeleteAPIVies(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    
class PostCreateAPIVies(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer