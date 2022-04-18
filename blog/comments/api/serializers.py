from rest_framework import serializers
# from rest_framework.serializers import HyperlinkedIdentityField
from django.contrib.contenttypes.models import ContentType

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    reply_count = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'content',
            'reply_count'
        ]
    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
        
class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp'
        ]
        
class CommentDetailSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'content',
            'child',
            'reply_count'
        ]
        
    def get_child(self,obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None
    
    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
    
 #esto porque usamos foreing key   
def create_comment(model_type='post', id=None, parent_id=None):
    class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                'id',
                'parent',
                'content',
                'timestamp'
            ]
        #con esto inicializo la clase
        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            self.id = id
            self.parent_obj = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count()==1:
                    self.parent_obj = parent_qs.first()
            return super(CommentCreateSerializer,self).__init__(*args,**kwargs)
        #se envia para validar como si fuera una forma  
        def validate(self,data):
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model = model_type)  
            if not model_qs.exists() or model_qs.count() != 1:
                raise serializers.ValidationError('This is not a valid content type')
            SomeModel = model_qs.first().model_class() 
            obj_qs = SomeModel.objects.filter(id=self.id) #error
            if not obj_qs.exists() or obj_qs.count()!=1:
                raise serializers.ValidationError('This is not a id for this content type')
            return data
        #esto luego de ser enviada y validada se usa toda es informacion
        def create(self,validate_data):
            content = validated_data.get('content')
            model_type = self.model_type
            id = self.id
            parent_obj = self.parent_obj
            comment = Comment.objects.create_by_model_type(
                model_type, id, content,
                parent_obj=parent_obj
                )
            return comment 
                
    
    return CommentCreateSerializer