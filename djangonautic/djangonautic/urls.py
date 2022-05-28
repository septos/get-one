"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from . import views            #masukan link ke views.py

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),         #menuju link ke fungsi about
    url(r'^$', views.homepage),           #menuju link ke fungsi homepage
    #mendaftarkan app article pada url di settingan url utama
    url(r'^articles/', include('articles.urls')),
    
]
