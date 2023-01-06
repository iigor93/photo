from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('subscribe/', views.Subscribe.as_view(), name='subscribe'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('api_load/', views.APILoadView.as_view(), name='api_load'),
]
