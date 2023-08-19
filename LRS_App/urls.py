from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('home', views.home, name = 'home' ),
    path('about', views.about, name = 'about'),
    path('loginUser', views.loginUser, name = 'loginUser'),
    path('contact', views.contact, name = 'contact'),
    path('plans', views.plans, name = 'plans'),
    path('register', views.register, name = 'register'),
    path('upload_files', views.upload_files, name = 'upload_files'),
    path('logoutUser', views.logoutUser, name = 'logoutUser'),
    path('standard', views.standard, name = 'standard'),
    path('premium', views.premium, name = 'premium'),
    path('business', views.business, name = 'business'),
    path('vip', views.vip, name = 'vip'),
    path('myplan', views.myplan, name = 'myplan'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)