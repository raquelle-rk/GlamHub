from django.db import models

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class ContactUs(models.Model):
    message_name = models.CharField(max_length=255, null=False, blank=False)
    message = RichTextUploadingField(max_length=5000, null=False, blank=False)
    message_email = models.EmailField(max_length=70, blank=False, null=False)
