from django.conf.urls import url
from . import views            #masukan link ke views.py

urlpatterns = [
    url(r'^$', views.article_list),
#    path('', views.article_list),           #menuju link ke fungsi homepage
]
