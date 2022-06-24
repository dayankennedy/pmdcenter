from django.shortcuts import render

def base(request):
    return render(request ,'base.html')

def index(request):
    return render(request ,'index.html')

def about(request):
    return render(request ,'about.html')

def appoinment(request):
    return render(request ,'appoinment.html')


def blog_sidebar(request):
    return render(request ,'blog_sidebar.html')

def blog_single(request):
    return render(request ,'blog_single.html')


def department(request):
    return render(request ,'department.html')

def contact(request):
    return render(request ,'contact.html')

def department_single(request):
    return render(request ,'department_single.html')


def doctor(request):
    return render(request ,'doctor.html')

def doctor_single(request):
    return render(request ,'doctor_single.html')


def service(request):
    return render(request ,'service.html')

def confirmation(request):
    return render(request ,'confirmation.html')

