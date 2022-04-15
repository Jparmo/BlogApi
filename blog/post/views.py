from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q 

from django.contrib.contenttypes.models import ContentType
# Create your views here.
from .models import Post
from .forms import PostForm
from comments.models import Comment

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
    comments = Comment.objects.filter(content_type= content_type, object_id=obj_id)
    context = {
        "instance":instance,
        "title": instance.title,
        'comments':comments
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
    