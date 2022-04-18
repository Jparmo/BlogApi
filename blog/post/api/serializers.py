from rest_framework import serializers
# from rest_framework.serializers import HyperlinkedIdentityField

from post.models import Post


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'post-api:detail',
        #read_only = True,
        lookup_field = 'pk'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name = 'post-api:delete',
        #read_only = True,
        lookup_field = 'pk'
    )
    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'content',
            'delete_url'
        ]
        
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content'
        ]
        
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]