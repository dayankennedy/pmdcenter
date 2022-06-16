from django.shortcuts import render



def home(request):
    return render(request ,'home.html')

def about(request):
    return render(request ,'about.html')
def index(request):
    return render(request ,'index.html')

def home(request):
    return render(request ,'about.html')

def appoinment(request):
    return render(request ,'appoinment.html')


def blog_sidebar(request):
    return render(request ,'blog_sidebar.html')

def home(request):
    return render(request ,'blog-single.html')
def home(request):
    return render(request ,'department.html')

def home(request):
    return render(request ,'department-single.html')


def home(request):
    return render(request ,'doctor.html')
def home(request):
    return render(request ,'doctor-single.html')


def home(request):
    return render(request ,'service.html')