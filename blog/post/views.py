from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q 

from django.contrib.contenttypes.models import ContentType
# Create your views here.
from .models import Post
from .forms import PostForm
from comments.models import Comment
from comments.forms import CommentForm

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #usa la funcion hecha en el modelo y te muestra lo que publicaste
        return HttpResponseRedirect(instance.get_url())
    context = {
        'form': form,
    }
    return render(request, 'post.html', context)

def post_individual(request, id):
    instance = get_object_or_404(Post, id=id)
    content_type = ContentType.objects.get_for_model(Post)
    obj_id = instance.id
    #Se trabaja con la caja de comentarios al post
    initial_data = {
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }
    comment_form = CommentForm(request.POST or None,initial=initial_data)
    if comment_form.is_valid():
        obj_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get('content')
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
            content_type = content_type,
            object_id = obj_id,
            content = content_data,
            parent = parent_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_url())
    
    comments = Comment.objects.filter(content_type= content_type, object_id=obj_id).filter(parent=None)
    context = {
        "instance":instance,
        "title": instance.title,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request, 'detail.html', context)

def post_list(request):
    queryset = Post.objects.all()
    query = request.GET.get("search")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
            ).distinct()
    context = {
        "publish":queryset,
        "title": "List"
    }
    return render(request, 'lista.html', context)

def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #devuelve un msg
        return HttpResponseRedirect(instance.get_url())
    context = {
        "instance":instance,
        "title": instance.title,
        "form": form
    }
    return render(request, 'post.html', context)


def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect('list')
    