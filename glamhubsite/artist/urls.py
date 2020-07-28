from django.urls import path
from artist.views import (
    create_artistportfolio_view,
    detail_artistportfolio_view,
    edit_artistportfolio_view,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_artistportfolio_view, name="create"),
    path('<slug>/', detail_artistportfolio_view, name="detail"),
    path('<slug>/edit/', edit_artistportfolio_view, name="edit"),
]
