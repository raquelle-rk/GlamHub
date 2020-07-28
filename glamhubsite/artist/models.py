from django.db import models
from phone_field import PhoneField

from django.utils.text import slugify
from django.conf import settings
# from django.db.models.signals import post_delete
# from django.dispatch import receiver


# method to define the upload location for images associated with blog posts
def upload_location(instance, filename, **kwargs):
    file_path = 'artist/{business_owner_id}/{business_name}-{filename}'.format(
            business_owner_id=str(instance.business_owner.id),
            business_name=str(instance.business_owner),
            filename=filename
        )
    return file_path

# define a constant (tuple choices to keep status of the business.)
STATUS = [ # noqa
    ('A', 'Active'),
    ('I', 'Inactive'),
]


class ArtistPortfolio(models.Model):
    ArtistryCategory = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200)
    business_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # noqa
    profile_image = models.ImageField(upload_to='pics')
    email_address = models.EmailField(max_length=70, blank=True, null=True)
    phone_number = PhoneField(null=False, blank=False, unique=True)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(blank=True, null=True, unique=True)
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        verbose_name = "Artist Portfolio"
        verbose_name_plural = "Artist Porfolios"
        ordering = ['business_owner', 'business_name']

    # methods
    def __str__(self):
        return self.business_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.business_name + "-" + self.business_owner.username) # noqa
        super().save(*args, **kwargs)

    # # to delete images associated with a blog post that is deleted
    # @receiver(post_delete, sender=business_owner)
    # def submission_delete(sender, instance, **kwargs):
    #     instance.image.delete(False)


# class Contactus(models.Model):
#     message_name = models.CharField(max_length=200)
#     message_email = models.EmailField(max_length=70, blank=True, null=True)
#     message = models.CharField(max_length=5000)
