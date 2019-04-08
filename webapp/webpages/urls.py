from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView, name="homepage"),
    path('terms', views.TermsView, name="terms"),
    path('docs',views.Docs,name="docs"),
]
