from django.contrib import admin

from price.models import Price, Faq


class PriceAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {"fields": ("name", "price",
                           "duration",
                           "description_1",
                           "description_2",
                           "description_3",
                           "description_4",
                           )}),
    )
    list_display = ("name", "price")


class FaqAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {"fields": ("number", "title", "description",)}),
    )
    list_display = ("number", "title")


admin.site.register(Price, PriceAdmin)
admin.site.register(Faq, FaqAdmin)
