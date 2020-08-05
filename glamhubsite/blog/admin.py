from django.contrib import admin

from blog.models import BlogPost, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("participant_name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("participant_name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(BlogPost)
admin.site.register(Comment, CommentAdmin)
