
from geniusvoice import views
from django.contrib import admin
from django.urls import path
from . import faceCollect
from . import face_recognize
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', faceCollect.button, name='home'),
    path('', views.faceRecogntion, name='mainpage'),
    path('output/', faceCollect.output, name='script'),
    path('imgtrain', face_recognize.imgtrain, name='script2'),
    path('Teacherlogin/', views.Teacherlogin, name='attend'),
    # path('viewdata/', views.viewdata, name='data'),
    path('datewise/', views.datewise, name='date'),

    path('index/', views.SignupPage, name='signup'),
    path('index/login/', views.LoginPage, name='login'),
    # path('index/login/', views.Teacherlogin, name='attend'),wrong path
    #     path('index/login/collect/', (views.collect), name='collect'),
    path('index/login/collect/', login_required(views.collect), name='collect'),
    # protected url are
    path('Teacherlogin/studentData/', login_required(views.user_page),
         name='user_page'),
    # path('home/', views.home, name='home'),url not protected
    path('home/', login_required(views.home),
         name='home'),
    #     path('home/', (views.home),
    #          name='home'),

    # path('Teacherlogin/studentData/', views.user_page, name='user_page'),

    # path('login/Teacherlogin/', views.Teacherlogin, name='attend'),
    # path('index/login/Teacherlogin/', views.Teacherlogin, name='attend'),
    path('index/login/AttendView/', views.back_teacher, name='back_teacher'),

    # path('home/', views.HomePage, name='home'),
    path('', views.back_home, name='back_home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('', views.homepage, name='homepage'),
    # index page to sign up and login spage
    # path('student-login/', views.student_login, name='student_login'),
    # path('teacher-login/', views.teacher_login, name='teacher_login'),

    # path('index/login/collect/', views.collect, name='collect'),
    path('index/login/AttendView/',
         login_required(views.AttendView), name='AttendView'),
    #     path('index/login/AttendView/',
    #          login_required(views.AttendView), name='AttendView'),
    # path('Teacherlogin/DirectAttendView/',
    #      views.DirectAttendView, name='DirectAttendView'),
    # http://127.0.0.1:8000/Teacherlogin/studentData/
    # http://127.0.0.1:8000/index/login/AttendView/


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# python manage.py makemigrations
# python manage.py migrate
