import math

from django.shortcuts import render
from django.views import View

from price.models import Price, Faq


class PriceView(View):
    template_name = "price/pricing.html"

    def get(self, request, *args, **kwargs):
        prices = Price.objects.all()
        faqs = Faq.objects.all()

        context = {"prices": prices, "breadcrumb": "Цена"}

        if faqs:
            faq_half = math.ceil(faqs.count()/2)
            context["faq"] = faqs
            context["faq_half"] = faq_half

        return render(request, self.template_name, context=context)

