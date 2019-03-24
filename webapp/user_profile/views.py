from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from user_profile.forms import UserProfileModelForm, UserDetailModelForm, StudentForm, MessmanagerForm
from django.contrib.auth.models import User

from user_profile.models import Student, Messmanager

# Create your views here.


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/profile.html"

    def post(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = user_profile_form = UserProfileModelForm(request.POST, request.FILES,
                                                                                instance=request.user.user_profile)
        print(request.POST)
        context['user_detail_form'] = user_detail_form = UserDetailModelForm(request.POST,
                                                                             instance=request.user)
        if 'is_student' in request.POST:
            context['student_form'] = student_form = StudentForm(request.POST,instance=request.user.Student)
            context['messmanager_form'] = True
        else:
            context['student_form'] = True
            context['messmanager_form'] = messmanager_form = MessmanagerForm(request.POST,instance=request.user.Messmanager)
        if user_profile_form.is_valid() and user_detail_form.is_valid():
            if request.user.user_profile.is_student :
                if student_form.is_valid():
                    student_form.save()
                else:
                    print(student_form.errors, "Error in Student form ")
            else:
                if messmanager_form.is_valid():
                    messmanager_form.save()
                else:
                    print(messmanager_form.errors, "Error in Mess Manager Form")
            user_profile_form.save()
            user_detail_form.save()
            print(request.POST)
            return redirect(reverse('homepage'))
        else:
            print(user_profile_form.errors, "++++++")

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = UserProfileModelForm(instance=request.user.user_profile)
        context['user_detail_form'] = UserDetailModelForm(instance=request.user)
        current_user = User.objects.get(id = request.user.id)
        is_student = current_user.user_profile.is_student
        context['is_student'] = is_student
        if is_student:
            context['student_form'] = StudentForm(instance=request.user.Student)
        else:
            context['messmanager_form'] = MessmanagerForm(instance=request.user.Messmanager)
        return render(request, self.template_name, context=context)


class UserStatusView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/status.html"

def dashboard(request):
    current_user = User.objects.get(id = request.user.id)
    is_student = current_user.user_profile.is_student
    if is_student:
        user = current_user.Student
    else:
        user = current_user.Messmanager
    return render(request,"user_profile/dashboard.html",{'user':user, 'current_user':current_user})

def profile_view(request):
    current_user = User.objects.get(id = request.user.id)
    is_student = current_user.user_profile.is_student
    if is_student:
        user = current_user.Student
    else:
        user = current_user.Messmanager
    return render(request,"user_profile/result.html",{'user':user, 'current_user':current_user})