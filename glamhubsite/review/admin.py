from django.contrib import admin

from review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "portfolio", "created_on")
    list_filter = ("name", "created_on")
    search_fields = ("participant", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Review, ReviewAdmin)
