# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
from django.shortcuts import get_object_or_404
import markdown
from comments.forms import CommentForm

# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={
        'title' : 'Our Blog',
        'welcome' : 'Welcome to our blog!',
        'post_list' : post_list,
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions = [
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()

    return render(request, 'blog/detail.html', context = {'post' : post,
                                                          'form' : form,
                                                          'comment_list' : comment_list,})

def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year = year,
                                    create_time__month = month,
                                    ).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list' : post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk = pk)
    post_list = Post.objects.filter(category = cate).order_by('-create_time')
    return render(request, 'blog/index.html', context = {'post_list' : post_list})
