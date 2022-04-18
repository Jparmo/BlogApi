from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


from post.models import Post

# Create your models here.

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs
    
    def create_by_model_type(self,model_type,id,content,parent_obj=None):
        model_qs = ContentType.objects.filter(model = model_type)  
        if model_qs.exists():
            SomeModel = model_qs.first().model_class() 
            obj_qs = SomeModel.objects.filter(id=id) #error
            if obj_qs.exists() and obj_qs.count()==1:
                instance = self.model()
                instance.content = content
                instance.content_type = model_qs.first()
                instances.object_id = obj_qs.first().id
                if parent_obj:
                    instance.parent = parent_obj
                instance.save()
                return instance 
        return None

class Comment(models.Model):
    name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    #nueva foregin para hacer hijos de comentarios
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("thread", kwargs={'id':self.id})
    
    
    #instance method, para responder
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @property
    def is_parent(self):
        if self.parent is not None:
            return False 
        return True