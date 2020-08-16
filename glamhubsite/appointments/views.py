from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, ListView

from artist.models import ArtistPortfolio

from .forms import AppointmentForm
from .models import Appointment


class AppointmentCreateView(View):
    template_name = 'appointments/appointment_create.html'
    form_class = AppointmentForm

    def get(self, request, *args, **kwargs):
        portfolio = get_object_or_404(ArtistPortfolio, slug=kwargs['slug'])
        booked_dates = Appointment.objects.filter(
            artist=portfolio.business_owner, is_approved=True).order_by(
                'appointment_date').values_list('appointment_date', flat=True)
        blocked_dates = [date.strftime('%d/%m/%Y') for date in booked_dates]
        form = self.form_class(
            initial={
                'artist': portfolio.business_owner,
                'portfolio': portfolio
            }
        )
        context = {
            'blocked_dates': blocked_dates,
            'form': form
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        portfolio = get_object_or_404(ArtistPortfolio, slug=kwargs['slug'])
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                appointment = form.save(commit=False)
                appointment.artist = portfolio.business_owner
                appointment.save()
                messages.success(request, "Appointment created successfully.")
                url = reverse_lazy('artist:detail', kwargs={'pk': portfolio.slug})
                return redirect(url)
            except Exception:
                messages.error(request, "Appointment was not updated. Please try again.")
                form = self.form_class(
                    initial={
                        'artist': portfolio.business_owner,
                        'portfolio': portfolio,
                        'appointment_date': appointment.appointment_date,
                        'description': appointment.description
                    }
                )
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


def approve_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if appointment.artist == request.user:
        appointment.is_approved = True
        appointment.save()
        # redirect to appointments list for artist
        # redirect to appointment detail view
    else:
        # redict back to same page without changes
        pass
