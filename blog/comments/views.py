from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect


from .models import Comment
from .forms import CommentForm

# Create your views here.

def comment_thread(request, id):
    obj =  get_object_or_404(Comment, id=id)
    
    
    content_object = obj.content_object
    content_id = obj.content_object.id    
    #Se trabaja con la caja de comentarios al post
    initial_data = {
        'content_type': obj.content_type,
        'object_id': obj.object_id
    }
    form = CommentForm(request.POST or None,initial=initial_data)
    if form.is_valid():
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        
        except:
            parent_id = None
            
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()
                
        new_comment, created = Comment.objects.get_or_create(
            #name = name,
            content_type = obj.content_type,
            object_id = obj_id,
            content = content_data,
            parent = parent_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_url())
    
    
    context = {
        'comment':obj,
        'form': form
    }
    
    
    return render(request, 'comment_thread.html',context)
