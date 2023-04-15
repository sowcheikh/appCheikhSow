"""devoirSowCheikh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from appCheikhSow import views

urlpatterns = [
    path('', views.index, name='index'),
    path('presentation', views.presentation, name='presentation'),
    path('tome1', views.tome1, name='tome1'),
    path('tome2', views.tome2, name='tome2'),
    path('contact', views.contact, name='contact'),
    path('thanks', views.thanks, name='thanks'),
    path('to_admin', views.to_admin, name="to_admin"),
    path('admin', admin.site.urls, name="admin"),
    path('adminlogout/', views.signout, name="logout"),
    path('home/', include('appCheikhSow.urls')),
]
