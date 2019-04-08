from django.views.generic import TemplateView


# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from user_profile.forms import UserProfileModelForm, UserDetailModelForm, StudentForm, MessmanagerForm
from django.contrib.auth.models import User

def HomePageView(request):
    template_name = "webpages/homepage.html"
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        if current_user.Student.is_scanned :
            current_user.Student.is_scanned = False
            current_user.Student.save()
    return render(request,template_name)

def TermsView(request):
    template_name = "webpages/terms.html"
    return render(request,template_name)

def Docs(request):
    return render(request,"webpages/docs.html")
