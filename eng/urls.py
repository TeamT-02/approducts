from django.urls import path
from . import views
from rus.viewss import index_ru, about_ru, product_ru, product_detail_ru, contacts_ru, certificate_ru, \
    certificate_detail_ru
from uzb.views import index_uz, about_uz, product_uz, product_detail_uz, certificate_detail_uz, certificate_uz, \
    contacts_uz


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('product_detail/<str:id>/', views.product_detail, name='product_detail'),
    path('contact', views.contacts, name='contact'),
    path('certificate', views.certificate, name='certificate'),
    path('certificate_detail/<str:id>/', views.certificate_detail, name='certificate_detail'),

    # rus
    path('ru', index_ru, name='index_ru'),
    path('about/ru', about_ru, name='about_ru'),
    path('product/ru', product_ru, name='product_ru'),
    path('product_detail/<str:id>/ru', product_detail_ru, name='product_detail_ru'),
    path('contact/ru', contacts_ru, name='contact_ru'),
    path('certificate/ru', certificate_ru, name='certificate_ru'),
    path('certificate_detail/<str:id>/ru', certificate_detail_ru, name='certificate_detail_ru'),

    # uz
    path('uz', index_uz, name='index_uz'),
    path('about_uz', about_uz, name='about_uz'),
    path('product_uz', product_uz, name='product_uz'),
    path('product_detail/<str:id>/uz', product_detail_uz, name='product_detail_uz'),
    path('contact_uz', contacts_uz, name='contact_uz'),
    path('certificate_uz', certificate_uz, name='certificate_uz'),
    path('certificate_detail/<str:id>/_uz', certificate_detail_uz, name='certificate_detail_uz'),
]
