from django import forms

from artist.models import ArtistPortfolio


# create artistportfolio form
class CreateArtistPortfolioForm(forms.ModelForm):

    class Meta:
        model = ArtistPortfolio
        fields = ['business_name', 'description', 'profile_image']


class UpdateArtistPortfolioForm(forms.ModelForm):

    class Meta:
        model = ArtistPortfolio
        fields = ['business_name', 'description', 'profile_image']

    # custom edit and save method of existing profile
    def save(self, commit=True):
        artistportfolio = self.instance
        artistportfolio.business_name = self.cleaned_data['business_name']
        artistportfolio.description = self.cleaned_data['description']

        # if there is a new image set it
        if self.cleaned_data['profile_image']:
            artistportfolio.image = self.cleaned_data['profile_image']

        if commit:
            artistportfolio.save()
        return artistportfolio


# class ContactUsForm(forms.ModelForm):

#     class Meta:
#         model = ArtistPortfolio
#         fields = ['message_name', 'message_email', 'message']














