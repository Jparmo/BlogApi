from django.contrib import admin
# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_displat = ['title','updated','timestamp']
    list_filter = ['updated','timestamp']
    list_editable = ['title', 'content']
    search_fields = ['title', 'content']
    # metadata options
    class Meta:
        model = Post

admin.site.register(Post)