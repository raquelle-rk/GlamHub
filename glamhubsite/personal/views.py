from django.shortcuts import render, redirect, get_object_or_404
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail


from blog.views import get_blog_queryset
from artist.views import get_artistportfolios_queryset  # noqa
from artist.models import ArtistPortfolio
from blog.forms import CommentForm
# from artist.forms import ContactUsForm
from blog.models import BlogPost


def home_screen_view(request):
    # context = {}

    # # to accept queries
    # query = ""
    # if request.GET:
    #     query = request.GET.get('q', '')
    #     context['query'] = str(query)

    # blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True) # noqa

    # # pagination for all website pages
    # page = request.GET.get('page', 1)
    # blog_posts_paginator = Paginator(blog_posts, BLOG_POST_PER_PAGE)

    # try:
    #     blog_posts = blog_posts_paginator.page(page)
    # except PageNotAnInteger:
    #     blog_posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    # except EmptyPage:
    #     blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    # context['blog_posts'] = blog_posts
    return render(request, "personal/index.html")


def about_us_view(request):
    return render(request, "personal/about.html")


BLOG_POST_PER_PAGE = 5


def blog_posts_view(request, *args, **kwargs):
    context = {}

    # to accept queries
    # query = ""
    # if request.GET:
    #     query = request.GET.get('q', '')
    #     context['query'] = str(query)

    # blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)  # noqa

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
   

    # comments = blog_posts.comments.filter(active=True)
    # new_comment = None
    # # Comment posted
    # if request.method == "POST":
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():

    #         new_comment = comment_form.save(commit=False)
    #         new_comment.post = blog_posts
    #         new_comment.save()
    #     else:
    #         comment_form = CommentForm()

    # pagination for all website pages
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POST_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "personal/blog_posts.html", context)
    # return render(request, "personal/blog_posts.html", {"post": post, "comments": comments, "new_comment": new_comment, "comment_form": comment_form})


ARTISTPORTOFOLIOS_PER_PAGE = 5


def artist_portfolio_screen(request, *args, **kwargs):
    context = {}

    # to accept queries
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    # artistportfolios = sorted(get_artistportfolios_queryset(query), key=attrgetter('id'), reverse=True) # noqa
    artistportfolios = sorted(get_artistportfolios_queryset(query), key=attrgetter('business_name'), reverse=True)  # noqa
    context['artistportfolios'] = artistportfolios

    # pagination for all website pages
    page = request.GET.get('page', 1)
    artistportfolios_paginator = Paginator(artistportfolios, ARTISTPORTOFOLIOS_PER_PAGE)  # noqa

    try:
        artistportfolios = artistportfolios_paginator.page(page)
    except PageNotAnInteger:
        artistportfolios = artistportfolios_paginator.page(ARTISTPORTOFOLIOS_PER_PAGE)  # noqa
    except EmptyPage:
        artistportfolios = artistportfolios_paginator.page(artistportfolios_paginator.num_pages)  # noqa

    context['artistportfolios'] = artistportfolios

    return render(request, "personal/artist_portfolios.html", context)


def contact_us_view(request):

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['glamhubsupport@gmail.com']  # to Email
        )

        return render(request, 'personal/contact_us.html', {'message_name': message_name})  # noqa
    else:
        return render(request, 'personal/contact_us.html', {})


def services_screen_view(request):

    return render(request, "personal/services.html", {})


# def SearchResultsView(request):
#     model = BlogPost
#     template_name = 'search_results.html'
