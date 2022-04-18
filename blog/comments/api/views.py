from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from comments.models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer, create_comment
from django.db.models import Q 
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    #query title and content using rest framework
    filter_b = [SearchFilter, OrderingFilter]
    search_fields = ['content']
    
    def get_queryset(self, *args, **kwargs):
        #queryset =  super(PostListAPIView, self).get_queryset(*args,**kwargs)
        queryset = Comment.objects.all()
        query = self.request.GET.get("q")
        # query title and content using django
        if query:
            queryset = queryset.filter(
            Q(content__icontains=query)
            ).distinct()
        return queryset
    
class CommentDetailAPIVies(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    # lookup_field = 'id'
    
# class PostUpdateAPIVies(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
    
# class PostDeleteAPIVies(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
    
class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    #serializer_class = PostCreateUpdateSerializer
    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        id = self.request.GET.get('id')
        parent_id = self.request.GET.get('parent_id',None)
        return create_comment(model_type=model_type, id=id, parent_id=parent_id)