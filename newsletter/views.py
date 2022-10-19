from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'newsletter/dashboard.html')


def newsletter(request):
    return render(request, 'newsletter/newsletter.html')
