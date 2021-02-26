from django.shortcuts import render, HttpResponse


# Create your views here.

def Homepage(request):
    return render(request, 'pages/index.html')


def About_page(request):
    return render(request, 'pages/about.html')
