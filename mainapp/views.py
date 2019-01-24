from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
