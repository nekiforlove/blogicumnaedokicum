from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    template_name = 'blog/index.html'
    posts = (
        Post.published().order_by('-pub_date')[:5]
    )
    context = {
        'post_list': posts
    }
    return render(
        request,
        template_name=template_name,
        context=context
    )


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.published().filter(id=post_id)
    )
    context = {
        'post': post
    }
    return render(
        request,
        template_name=template_name,
        context=context
    )


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = (
        Post.published().filter(
            category=category
        ).order_by('-pub_date')
    )
    context = {
        'category': category,
        'post_list': posts
    }
    return render(
        request,
        template_name=template_name,
        context=context
    )
