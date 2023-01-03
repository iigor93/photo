import math

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from core.models import Carousel, Advantage, Portfolio, SubscribeEmail, Contact, About
from price.models import Faq


class Index(View):
    template_name = "core/index.html"

    def get(self, request):
        carousel = Carousel.objects.filter(active=True)
        advantages = Advantage.objects.filter(active=True)
        portfolio = Portfolio.objects.prefetch_related("category").filter(active=True)
        categories = []
        for item in portfolio:
            cat = list(item.category.all())
            categories.extend(cat)
        categories = list(set(categories))

        context = {
            "carousel": carousel,
            "advantages": advantages,
            "portfolio": portfolio,
            "categories": categories,
            "home": True,
            "breadcrumb": "Home"
        }

        return render(request, self.template_name, context=context)


class Subscribe(View):
    def post(self, request, *args, **kwargs):
        # print(request.POST)

        email = request.POST.get("email")
        try:
            SubscribeEmail.objects.create(email=email)
        except BaseException as e:
            print(e)

        return HttpResponseRedirect(reverse("index"))


class ContactView(View):
    template_name = "core/contact.html"

    def get(self, request, *args, **kwargs):
        context = {"contact": Contact.objects.all().last(), "breadcrumb": "Контакты"}
        return render(request, self.template_name, context=context)


class AboutView(View):
    template_name = "core/about.html"

    def get(self, request, *args, **kwargs):
        about = About.objects.all().last()

        context = {"breadcrumb": "О нас", "about": about}
        return render(request, self.template_name, context=context)


class ServiceView(View):
    template_name = "core/services.html"

    def get(self, request, *args, **kwargs):
        advantages = Advantage.objects.filter(active=True)
        faqs = Faq.objects.all()
        context = {"breadcrumb": "Services",
                   "services": True,
                   "advantages": advantages}

        if faqs:
            faq_half = math.ceil(faqs.count()/2)
            context["faq"] = faqs
            context["faq_half"] = faq_half

        return render(request, self.template_name, context=context)
