from django.contrib import admin

from core.models import Carousel, Advantage, Category, Portfolio, SubscribeEmail, Contact, About


class CarouselAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'title', 'text', 'link', 'active')}),
    )
    list_display = ('image_thumb', 'title', 'text', 'link', 'active')


class AdvantageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'title', 'text', 'active')}),
    )
    list_display = ('image_thumb', 'title', 'text', 'active')


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'name',)}),
    )
    list_display = ('image_thumb', 'name',)


class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'title', 'category', 'wh_class', 'active')}),
    )
    list_display = ('image_thumb', 'title', 'wh_class', 'active')


class SubscribeEmailAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'date', "delete_code")}),
    )
    readonly_fields = ('date', "email", "delete_code")
    list_display = ('email', 'date')


class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'address', "phone")}),
    )
    list_display = ('email', 'address', 'phone')


class AboutAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'title', "text")}),
    )
    list_display = ('title',)


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(SubscribeEmail, SubscribeEmailAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
