from django.contrib import admin

from blog.models import BlogPost, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("participant_name", "body", "post", "created_on", "approved_comment")
    list_filter = ("approved_comment", "created_on")
    search_fields = ("participant_name", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(BlogPost)
admin.site.register(Comment, CommentAdmin)
