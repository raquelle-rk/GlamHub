"""glamhubsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

# from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views

from personal.views import (
    home_screen_view,
    about_us_view,
    blog_posts_view,
    artist_portfolio_screen,
    contact_us_view,
    services_screen_view,


    )

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
)
from artist.views import (
    create_artistportfolio_view,
    detail_artistportfolio_view,
    edit_artistportfolio_view,
)

from appointments.views import approve_appointment, reject_appointment

urlpatterns = [
    path('', home_screen_view, name="home"),
    path('about/', about_us_view, name="about"),
    path('account/', account_view, name="account"),
    path('admin/', admin.site.urls),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'), # noqa
    path('ckeditor/browser/', never_cache(login_required(views.browse)), name='ckeditor_browse'), # noqa
    path('posts/', blog_posts_view, name="post"),
    path('blog/', include('blog.urls', 'blog')),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),  # noqa
    path('register/', registration_view, name="register"),
    path('artist/', include('artist.urls', 'artist')),  # noqa
    path('artist_portfolios/', artist_portfolio_screen, name="artist_portfolios"), # noqa
    path('contact_us/', contact_us_view, name="contact_us"),
    path('services/', services_screen_view, name="services"),
    path('appointments/', include('appointments.urls')),





    #  Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path(
        'password_reset/', auth_views.PasswordResetView.as_view(),
        name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),



    path(
        'appointment_approval/', approve_appointment),
    path(
        'appointment_reject/', reject_appointment),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # noqa
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # noqa
