from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
# from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from artist.models import ArtistPortfolio
from account.models import Account
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import AppointmentForm
from .models import Appointment


class AppointmentCreateView(LoginRequiredMixin, View):
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
                appointment.portfolio = portfolio
                appointment.client = request.user
                appointment.save()

                messages.success(request, "Appointment created successfully. An email will be sent to you once your submission is reviewed ")
                url = reverse_lazy('artist:detail', kwargs={
                                   'slug': portfolio.slug})
                return redirect(url)
            except Exception:
                messages.error(
                    request, "Appointment was not updated. Please try again.")
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


@login_required()
def list_appointments(request, slug):
    template_name = 'appointments/appointment_list.html'
    queryset = Appointment.objects.filter(
        portfolio__slug=slug, artist=request.user).order_by('-appointment_date')
    return render(request, template_name, {'appointments': queryset})


@login_required()
def approve_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if appointment.artist == request.user:
        print("approving")
        appointment.is_approved = True
        appointment.save()
        messages.success(request, "Appointment approved. An email will be sent to the client")
       #  send email to appointment.client.email
        subject = 'Appointment Feedback'
        message = None
        from_email = 'glamhubsite.com'
        html_message = render_to_string(
            'feedback/appointment_approval_email.html',
            context={
                'client': appointment.client.username,
                'business_name': appointment.portfolio.business_name
            }
        )
        try:
            send_mail(
                subject, message, from_email,
                [appointment.client.email, request.user.email],
                html_message=html_message)
        except Exception:
            pass
        url = reverse_lazy(
            'appointments:list',
            kwargs={'slug': appointment.portfolio.slug}
        )
        return redirect(url)
    else:
        return redirect(request.get_full_path())


@login_required()
def reject_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if appointment.artist == request.user:
        print("rejecting")
        appointment.is_reject = True
        appointment.save()
        messages.error(request, "Appointment rejected. An email will be sent to the client")
       #  send email to appointment.client.email
        subject = 'Appointment Feedback'
        message = None
        from_email = 'glamhubsite.com'
        html_message = render_to_string(
            'feedback/appointment_rejection_email.html',
            context={
                'client': appointment.client.username,
                'business_name': appointment.portfolio.business_name
            }
        )
        try:
            send_mail(
                subject, message, from_email,
                [appointment.client.email, request.user.email],
                html_message=html_message)
        except Exception:
            pass
        url = reverse_lazy(
            'appointments:list',
            kwargs={'slug': appointment.portfolio.slug}
        )
        return redirect(url)
    else:
        return redirect(request.get_full_path())
