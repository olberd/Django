from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def main(request):
    content = {
        'title': 'магазин'
    }
    return render(request, 'mainapp/index.html', content)


def products(request: HttpRequest, id=0):

    return render(request, 'mainapp/products.html', {
                      'product_id': id
                  })


def contact(request):
    return render(request, 'mainapp/contact.html')
