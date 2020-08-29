from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
# from django.http import HttpResponse

from artist.models import ArtistPortfolio
from artist.forms import CreateArtistPortfolioForm, UpdateArtistPortfolioForm
from review.models import Review
from review.forms import ReviewForm
# from account.models import Account


@login_required()
def create_artistportfolio_view(request):
    context = {}

    form = CreateArtistPortfolioForm(request.POST or None, request.FILES or None)  # noqa
    if form.is_valid():
        obj = form.save(commit=False)
        obj.business_owner = request.user
        obj.save()
        context['success_message'] = "Portfolio Created Successfully"

        form = CreateArtistPortfolioForm()

    context['artistportfolio'] = form

    return render(request, 'artist/create_artistportfolio.html', context)


@login_required()
def detail_artistportfolio_view(request, slug):

    context = {}
    artistportfolio = get_object_or_404(ArtistPortfolio, slug=slug)
    context['artistportfolio'] = artistportfolio

    return render(request, 'artist/detail_artistportfolio.html', context)


@login_required()
def edit_artistportfolio_view(request, slug):

    context = {}

    artistportfolio = get_object_or_404(ArtistPortfolio, slug=slug)
    if request.POST:
        form = UpdateArtistPortfolioForm(
            request.POST or None,
            request.FILES or None,
            instance=artistportfolio
        )

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated Successfully"
            artistportfolio = obj

    form = UpdateArtistPortfolioForm(
        initial={
            "artistry_category": artistportfolio.artistry_category,
            "business_name": artistportfolio.business_name,
            "business_owner": artistportfolio.business_owner,
            "profile_image": artistportfolio.profile_image,
            "email_address": artistportfolio.email_address,
            "phone_number": artistportfolio.phone_number,
            "description": artistportfolio.description,
            "portfolio_images": artistportfolio.portfolio_images,
            "status": artistportfolio.status,

        }
    )

    context['artistportfolioform'] = form

    return render(request, 'artist/edit_artistportfolio.html', context)

    artistportfolio = get_object_or_404(ArtistPortfolio, slug=slug)
    context['artistportfolioform'] = form

    return render(request, 'artist/edit_artistportfolio.html', context)


@login_required()
def add_review_to_portfolio(request, pk):
    portfolio = get_object_or_404(ArtistPortfolio, pk=pk)
    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.portfolio = portfolio
            review.name = request.user
            review.save()

            messages.success(request, "Review created successfully ")
            url = reverse_lazy('artist:detail', kwargs={
                               'slug': portfolio.slug})
            return redirect(url)

    form = ReviewForm(
        initial={
            'portfolio': portfolio
        }
    )
    return render(request, 'reviews/add_review.html', {'form': form})


# method to get a queryset based on a particular search
def get_artistportfolios_queryset(query=None):
    queryset = []
    queries = query.split(" ")  # how to clean would be [how, to, clean]
    for q in queries:
        portfolios = ArtistPortfolio.objects.filter(
            Q(business_name__icontains=q) |
            Q(description__icontains=q)
        ).distinct()

        for portfolio in portfolios:
            queryset.append(portfolio)

    # create unique set and then convert to list
    return list(set(queryset))
