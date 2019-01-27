import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post, Author
# Create your views here.

#the index function: gets a list of all the blogs, then returns that to the page
def index(request):
    all_blogs = Post.objects.all()
    authors = Author.objects.all()
    return render(request, 'blog/index.html', {'blog_list' : all_blogs, 'authors' : authors})

#postview function: returns the data for a specific post when accessed
#gets the specific post based off the id
def postview(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post' : post})

#createpost function: has two states, a POST and GET state
# the POST state will go through the data recieved and put together a blog 'post' object
# it will then redirect the user to the detail page for the newly created post
# 
# the GET state will get all the authors so that they can be used to create a list 
def createPost(request):
    if request.method == 'POST':
        post = Post()
        post.blog_title = request.POST['title']
        post.blog_author = Author.objects.get(pk=request.POST['author'])
        post.blog_post = request.POST['post']
        post.blog_date = datetime.datetime.now()
        post.save()
        num = Post.objects.latest('id')
        return HttpResponseRedirect(reverse('Post', args=(num.id,)))
    else:
        author = Author.objects.all()
        return render(request, 'blog/create.html', {'author' : author})

#editPost function: like the previous function it has a POST and GET state
# the POST state will go through the data recieved and put together a blog 'post' object
# it will then redirect the user to the detail page for the edited post
# 
# the GET state will get all the authors so that they can be used to create a list
# in addition it will also pass along the specifc post to pre-fill out the forms
def editPost(request, post_id):
    if request.method == 'POST':
        post = Post()
        post.id = post_id
        post.blog_title = request.POST['title']
        post.blog_author = Author.objects.get(pk=request.POST['author'])
        post.blog_post = request.POST['post']
        post.blog_date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect(reverse('Post', args=(post.id,)))
    else:
        post = get_object_or_404(Post, pk=post_id)
        author = Author.objects.all()
        return render(request, 'blog/edit.html', {'post' : post, 'author' : author})

#allows viewing of the authors info page, specific to that author
def authInfo(request, auth_id):
    author = get_object_or_404(Author, pk=auth_id)
    return render(request, 'blog/author.html', {'author' : author})