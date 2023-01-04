from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms
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


class BlogItemForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', max_length=255)
    content = forms.CharField(label='Текст страницы', widget=CKEditorWidget())


class BlogItemAdmin(admin.ModelAdmin):
    form = BlogItemForm

    fieldsets = (
        (None, {"fields": ("main_tag", "tags", "main_photo", "title",
                           "image",
                           "content",
                           "feature_post",
                           )}),
    )
    list_display = ("image_thumb", "title", "main_tag", "date")


admin.site.register(BlogTag, BlogTagAdmin)
admin.site.register(BlogImage, BlogImageAdmin)
admin.site.register(BlogItem, BlogItemAdmin)
