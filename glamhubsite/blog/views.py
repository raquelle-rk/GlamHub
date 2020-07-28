from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.http import HttpResponse

from blog.models import BlogPost
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
# from account.models import Account


@login_required()
def create_blog_view(request):
    context = {}

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        context['success_message'] = "Post Created Successfully"

        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, 'blog/create_blog.html', context)


@login_required()
def detail_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)


@login_required()
def edit_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.POST:
        form = UpdateBlogPostForm(
            request.POST or None,
            request.FILES or None,
            instance=blog_post
        )

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated Successfully"
            blog_post = obj

    form = UpdateBlogPostForm(
                initial={
                    "title": blog_post.title,
                    "body": blog_post.body,
                    "image": blog_post.image,
                }
            )

    context['form'] = form

    return render(request, 'blog/edit_blog.html', context)

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['form'] = form

    return render(request, 'blog/edit_blog.html', context)


# method to get a queryset based on a particular search
def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")  # how to clean would be [how, to, clean]
    for q in queries:
        posts = BlogPost.objects.filter(
                Q(title__icontains=q) |
                Q(body__icontains=q)
            ).distinct()

        for post in posts:
            queryset.append(post)

    # create unique set and then convert to list
    return list(set(queryset))
