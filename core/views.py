from django.shortcuts import render
from django.views import View

from core.models import Carousel, Advantage, Portfolio


class Index(View):
    template_name = "core/index.html"

    def get(self, request):
        carousel = Carousel.objects.filter(active=True)
        advantages = Advantage.objects.filter(active=True)
        portfolio = Portfolio.objects.filter(active=True)
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
