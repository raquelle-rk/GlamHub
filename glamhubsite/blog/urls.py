from django.urls import path
from blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    comment_approve,
    comment_remove,
    add_comment_to_post,
)
# from personal.view import SearchResultsView

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit/', edit_blog_view, name="edit"),
    path('posts/<int:pk>/comment/', add_comment_to_post, name='add_comment'), # noqa
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
]
