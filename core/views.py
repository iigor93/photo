from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from core.models import Carousel, Advantage, Portfolio, SubscribeEmail


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
        }

        return render(request, self.template_name, context=context)


class Subscribe(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)

        email = request.POST.get("email")
        try:
            SubscribeEmail.objects.create(email=email)
        except BaseException as e:
            print(e)

        return HttpResponseRedirect(reverse("index"))
