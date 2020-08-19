from django.db import models

from account.models import Account
from artist.models import ArtistPortfolio


class Appointment(models.Model):
    artist = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='artist')
    client = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='client',
        blank=True, null=True)
    portfolio = models.ForeignKey(
        ArtistPortfolio, on_delete=models.CASCADE,
        blank=True, null=True)
    appointment_date = models.DateField()
    description = models.TextField(blank=False, null=False, max_length=200,)
    is_approved = models.BooleanField(blank=True, null=True)

    class Meta:
        unique_together = ('artist', 'appointment_date')
