from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from posts.models import Hashtag, Post


def main_page_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }

        return render(request, 'posts/posts.html', context=context)


def hashtags_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags,
        }

        return render(request, 'posts/hashtags.html', context=context)
