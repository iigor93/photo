from django.contrib import admin

from blog.models import BlogTag, BlogImage, BlogItem


class BlogTagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ("name",)}),
    )
    list_display = ("name",)


class BlogImageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("image", "name")}),
    )
    list_display = ("image_thumb", "name")


class BlogItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("main_tag", "tags", "main_photo", "title",
                           "top_text",
                           "quote",
                           "description",
                           "last_description",
                           "image",
                           )}),
    )
    list_display = ("image_thumb", "title", "main_tag", "date")


admin.site.register(BlogTag, BlogTagAdmin)
admin.site.register(BlogImage, BlogImageAdmin)
admin.site.register(BlogItem, BlogItemAdmin)
