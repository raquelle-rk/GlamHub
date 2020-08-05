# from ckeditor.widgets import CKEditorWidget

from django import forms
# from django.forms import ModelForm

from blog.models import BlogPost, Comment


# create blogpost form
class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']


class UpdateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']

    # custom edit and save method of existing post
    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        # if there is a new image set it
        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']

        if commit:
            blog_post.save()
        return blog_post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('participant_name', 'email', 'body')













