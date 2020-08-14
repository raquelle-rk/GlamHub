from django.db import models

from account.models import Account
# from portfolio.models import ArtistPortfolio


class Appointment(models.Model):
    artist = models.ForeignKey(Account, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    description = models.TextField(blank=True, null=True, max_length=200)
    is_approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('artist', 'appointment_date')
