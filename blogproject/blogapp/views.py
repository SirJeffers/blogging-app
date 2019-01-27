import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post
# Create your views here.

def index(request):
    all_blogs = Post.objects.all()
    return render(request, 'blog/index.html', {'blog_list' : all_blogs})

def postview(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post' : post})

def createPost(request):
    if request.method == 'POST':
        post = Post()
        post.blog_title = request.POST['title']
        post.blog_author = request.POST['author']
        post.blog_post = request.POST['post']
        post.blog_date = datetime.datetime.now()
        post.save()
        num = Post.objects.latest('id')
        return HttpResponseRedirect(reverse('Post', args=(num.id,)))
    else:
        return render(request, 'blog/create.html')

def editPost(request, post_id):
    if request.method == 'POST':
        post = Post()
        post.id = post_id
        post.blog_title = request.POST['title']
        post.blog_author = request.POST['author']
        post.blog_post = request.POST['post']
        post.blog_date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect(reverse('Post', args=(post.id,)))
    else:
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'blog/edit.html', {'post' : post})