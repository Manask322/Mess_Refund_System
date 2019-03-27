from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from user_profile.forms import UserProfileModelForm, UserDetailModelForm, StudentForm, MessmanagerForm
from django.contrib.auth.models import User

from user_profile.models import Student, Messmanager
import datetime as dt
curr_time=dt.datetime.now().hour
# Create your views here.
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
is_scanned = False

def main():
    """
    A simple function that captures webcam video utilizing OpenCV. The video is then broken down into frames which
    are constantly displayed. The frame is then converted to grayscale for better contrast. Afterwards, the image
    is transformed into a numpy array using PIL. This is needed to create zbar image. This zbar image is then scanned
    utilizing zbar's image scanner and will then print the decodeed message of any QR or bar code. To quit the program,
    press "q".
    :return:
    """

    # Begin capturing video. You can modify what video source to use with VideoCapture's argument. It's currently set
    # to be your webcam.
    capture = cv2.VideoCapture(0)

    while True:
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        cv2.imshow('Current', frame)

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        image = Image.fromarray(gray)
        width, height = image.size
        # zbar_image = pyzbar.Imaimage   ge(width, height, 'Y800', image.tobytes())
        decoded=decode(image)
        if decoded != []:
            if decoded[0].data:
                val=decoded[0].data
                print(decoded,type(decoded),len(decoded))
                break
    cv2.destroyAllWindows()
    return val
        # # Scans the zbar image.
        # scanner = pyzbar.ImageScanner()
        # scanner.scan(zbar_image)

        # # Prints data from image.
        # for decoded in zbar_image:
        #     print(decoded.data)

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

meal_type = ["breakfast","lunch","snack","dinner","be hungry"]

def dashboard(request):
    global is_scanned
    current_user = User.objects.get(id = request.user.id)
    remaining_amount = 22000.0 - current_user.Student.refund
    cur_time=dt.datetime.now().hour
    print("time is",cur_time )
    if cur_time < 10 and cur_time > 7:
        meal="breakfast"
        meal_type=0
    elif cur_time > 10 and cur_time < 14:
        meal = "lunch"
        meal_type=1
    elif cur_time >= 16 and cur_time < 18 :
        meal = "snacks"
        meal_type =2
    elif cur_time > 18 and cur_time < 22:
        meal ="dinner"
        meal_type = 3
    else:
        meal="be hungry.."
        meal_type =4
    if meal_type==0:
        deduct = int(0.6 * 20)
    elif meal_type==1:
        deduct = int(0.6 * 40)
    elif meal_type == 2:
        deduct = int(0.6 * 10)
    elif meal_type == 3:
        deduct = int(0.6 * 30)
    else:
        deduct = 0
    if is_scanned:
        remaining_amount = remaining_amount - deduct
        is_scanned = False

    is_student = current_user.user_profile.is_student
    total_refund = current_user.Student.refund
    if is_student:
        user = current_user.Student
    else:
        user = current_user.Messmanager
    return render(request,"user_profile/dashboard.html",{'user':user, 'current_user':current_user,'refund':total_refund, 'meal':meal,"amount_remaining":remaining_amount,'meal_type':meal_type})

def profile_view(request):
    qr_val=main()
    qr_val=str(qr_val,"utf-8")
    len(qr_val)
    print(qr_val)
    if qr_val:
        is_scanned = True
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        first_name = current_user.first_name
        last_name = current_user.last_name
        picture = current_user.user_profile.image
        student_id = current_user.Student.student_id
        block = current_user.Student.block
        is_student = current_user.user_profile.is_student
        if is_student:
            user = current_user.Student
        else:
            user = current_user.Messmanager
        return render(request,"user_profile/result.html",{'user':user, 'current_user':current_user,'qr_val':qr_val})
    return redirect(reverse('homepage'))
