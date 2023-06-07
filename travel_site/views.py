from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    rows = Services.objects.all()[0:3]
    comments = Testimonial.objects.all()[0:3]

    context = {
        'rows' : rows,
        'comments': comments
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'services.html')
