from geniusvoice .face_recognize import imgtrain
from django.shortcuts import render
from geniusvoice .forms import ImageForm
from geniusvoice .models import Image
from .models import Image
from django.contrib.auth.models import User

from django.shortcuts import render
from .forms import ImageForm  # Import your ImageForm

from .models import Image

# sign in form
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms

# @login_required
# def my_protected_view(request):

# login code start

# @login_required(login_url='login')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        is_staff = request.POST.get('is_staff', 'false') == 'true'

        if pass1 != pass2:
            # error_message = "Your password and confirm password do not match."
            # return render(request, 'signup.html', {'error_message': error_message})
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(
                uname, email, pass1, is_staff=is_staff)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('AttendView')
            else:
                return redirect('collect')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


# login code end


def index(request):
    return render(request, 'index.html')


# form upload home function
def home(request):
    obj = None  # Initialize obj variable

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance  # Set obj to the uploaded image instance
            img = obj.photo

    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'upload.html', {'img': img, 'form': form, 'obj': obj})


def user_page(request):
    # Get all users excluding superusers and staff users
    users = User.objects.filter(is_superuser=False, is_staff=False)
    return render(request, 'studentData.html', {'users': users})


def back_home(request):
    return render(request, 'index.html')


def back_teacher(request):
    return render(request, 'TeacherLogin.html')

# simple redirecting to another page code


def faceRecogntion(request):
    return render(request, 'index.html')


def homepage(request):
    return render(request, 'index.html')


def collect(request):
    return render(request, 'collect.html')


def AttendView(request):
    return render(request, 'TeacherLogin.html')


def Teacherlogin(request):
    return render(request, 'login.html')


def datewise(request):
    return render(request, 'view_attendance.html')
