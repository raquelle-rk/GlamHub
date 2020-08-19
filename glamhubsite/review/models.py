from django.db import models

from account.models import Account


class Review(models.Model):
    portfolio = models.ForeignKey('artist.ArtistPortfolio', on_delete=models.CASCADE, related_name='reviews') # noqa
    name = models.ForeignKey(
        Account, on_delete=models.CASCADE,
        blank=True, null=True)
    body = models.TextField(help_text='Your review')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on', 'name']

    def __str__(self):
        return 'Reviewed {} by {}'.format(self.body, self.name)
