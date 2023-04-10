from django.urls import path
from .import views 


urlpatterns = [
    path('', views.index, name="index"),
    path('base/', views.base, name="home"),
    path('about/', views.about, name="about"),
    path('appoinment/', views.appoinment, name="appoinment"),
    path('blog_sidebar/', views.blog_sidebar, name="blog_siderbar"),
    path('blog_single/', views.blog_single, name="blog_single"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('contact/', views.contact, name="contact"),
    path('department/', views.department, name="department"),
    path('department_single/', views.department_single, name="department_single"),
    path('doctor/', views.doctor, name="doctor"),
    path('doctor_single/', views.doctor_single, name="doctor_single"),
    path('service/', views.service, name="service"),
]