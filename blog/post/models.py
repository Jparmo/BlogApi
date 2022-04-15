from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType



class Post(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('detail', kwargs={'id':self.id})
    
# Create your models here.

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
