from django import forms
from django.forms import ModelForm

from artist.models import ArtistPortfolio, ArtistryCategory
# from personal.models import ContactUs


# create artistportfolio form
class CreateArtistPortfolioForm(forms.ModelForm):
    artistry_category = forms.ModelChoiceField(
        queryset=ArtistryCategory.objects.filter(active=True),
        required=False
    )

    class Meta:
        model = ArtistPortfolio
        fields = '__all__'
        exclude = ('slug',)


class UpdateArtistPortfolioForm(forms.ModelForm):
    artistry_category = forms.ModelChoiceField(
        queryset=ArtistryCategory.objects.filter(active=True),
        required=False
    )

    class Meta:
        model = ArtistPortfolio
        fields = '__all__'
        exclude = ('slug',)

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


# class ContactUsForm(forms.Form):

#     class Meta:
#         fields = ['message_name', 'message_email', 'message']

#     def save(self, commit=True):
#         message_name = self.instance
#         message_email= self.cleaned_data['message_email']
#         message = self.cleaned_data['message']

#         if commit:
#             ContactUs.save()
#         return ContactUs














