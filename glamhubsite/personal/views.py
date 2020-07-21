from django.shortcuts import render
from account.models import Account


def home_screen_view(request):
    context = {}  # define context variable

    accounts = Account.objects.all()  # this will select all accounts in the db
    context['accounts'] = accounts
    return render(request, "personal/home.html", context)
