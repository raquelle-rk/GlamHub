from django.urls import path
from artist.views import add_review_to_portfolio, detail_artistportfolio_view
# from personal.view import SearchResultsView

app_name = 'review'

urlpatterns = [
    path('reviews/<int:pk>/review/', add_review_to_portfolio, name='add_review'), # noqa
    path('artist/<slug>/', detail_artistportfolio_view, name="detail"),
]

