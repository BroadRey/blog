from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from posts.forms import PostCreateForm
from posts.models import Hashtag, Post


def main_page_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'layouts/base.html')


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


def post_detail_view(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return render(request, 'posts/detail.html')

        context = {
            'post': post,
        }

        return render(request, 'posts/detail.html', context=context)


def post_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        context = {
            'form': PostCreateForm,
        }

        return render(request, 'posts/create.html', context)

    if request.method == 'POST':
        data, file = request.POST, request.FILES
        form = PostCreateForm(data, file)

        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                image=form.cleaned_data.get('image')
            )

            return redirect('/posts/')

        context = {
            'form': form,
        }

        return render(request, 'posts/create.html', context={'form': form})
