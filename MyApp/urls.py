from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
# from .views import GeneratePdf
app_name = "MyApp"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("login/", views.login, name="login"),
    # path("logint/", views.logint, name="logint"),
    # path("loginb/", views.loginb, name="loginb"),
    # # path("register/", views.register, name="register"),
    # path("logout/", views.logout, name="logout"),
    # path("dash/", views.dash, name="dash"),
    # path("dasht/", views.dasht, name="dasht"),
    # path("viewstudents/", views.viewstudents, name="viewstudents"),
    # path("view_stu_resume/<str:student_name>/", views.view_stu_resume, name="view_stu_resume"),
    # # path("tpo_add_stu/", views.tpo_add_student, name="tpo_add_student"),
    # # path("view_stu_resume/", views.view_stu_resume, name="view_stu_resume"),
    path("", views.create_resume, name="create_resume"),
   
    
    path("srt-resume/", views.create_resume, name="srt-resume"),

    




]