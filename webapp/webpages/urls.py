from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name="homepage"),
    path('terms', views.TermsView.as_view(), name="terms"),
]
