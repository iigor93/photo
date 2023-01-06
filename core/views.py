import math

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from core.models import Carousel, Advantage, Portfolio, SubscribeEmail, Contact, About, Category
from price.models import Faq


class Index(View):
    template_name = "core/index.html"

    def get(self, request):
        carousel = Carousel.objects.filter(active=True)
        advantages = Advantage.objects.filter(active=True)
        categories_list = Category.objects.prefetch_related("portfolio_set").all()
        categories_dict = {}
        for item in categories_list:
            categories_dict[item] = item.portfolio_set.all().count()
        portfolio = Portfolio.objects.prefetch_related("category").filter(active=True)[:5]
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
            "breadcrumb": "Home",
            "categories_dict": categories_dict,
        }

        return render(request, self.template_name, context=context)


class Subscribe(View):
    template_name = "core/unsubscribe.html"

    def get(self, request, *args, **kwargs):
        email = request.GET.get("email", None)
        code = request.GET.get("code", None)

        try:
            e = SubscribeEmail.objects.get(email=email, delete_code=code)
            e.delete()
            msg = f"Ваш email {email} удален из нашей рассылки."
        except ObjectDoesNotExist:
            msg = "Похоже Ваш email уже удален из рассылки."

        context = {"msg": msg}

        return render(request, self.template_name, context=context)

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


@method_decorator(csrf_exempt, name='dispatch')
class APILoadView(View):
    NUM_OF_PHOTO = 5

    def post(self, request, *args, **kwargs):
        print(request.POST)
        current_page = request.POST.get("page")
        try:
            current_page = int(current_page)
            last_page = Portfolio.objects.filter(active=True).count()
            response = "last" if current_page + self.NUM_OF_PHOTO >= last_page else "ok"
            portfolio = Portfolio.objects.filter(active=True)[current_page:current_page + self.NUM_OF_PHOTO]
            lst = []
            for item in portfolio:
                categories = list(item.category.all().values_list("name", flat=True))
                categories = " ".join(categories)

                lst.append([item.image.url, item.title, categories])

            return JsonResponse({response: lst}, safe=False)

        except BaseException as e:
            print(e)

        return JsonResponse({'err': []}, safe=False)


class PortfolioView(View):
    template_name = "core/portfolio.html"

    def get(self, request, *args, **kwargs):

        categories_list = Category.objects.prefetch_related("portfolio_set").all()
        categories_dict = {}
        for item in categories_list:
            categories_dict[item] = item.portfolio_set.all().count()
        portfolio = Portfolio.objects.prefetch_related("category").filter(active=True)[:5]
        categories = []
        for item in portfolio:
            cat = list(item.category.all())
            categories.extend(cat)
        categories = list(set(categories))

        context = {
            "portfolio": portfolio,
            "portfolio_menu": True,
            "categories": categories,
            "breadcrumb": "Portfolio",
            "categories_dict": categories_dict,
        }

        return render(request, self.template_name, context=context)