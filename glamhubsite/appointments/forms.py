from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    # appointment_date = forms.DateField(
    #     widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    appointment_date = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Appointment
        fields = ('appointment_date', 'description')
