from django.shortcuts import render
from django.http import HttpRequest
from .models import ProductCategory, Product


# Create your views here.

def main(request):
    # content = {'products': prod}
    main_menu = [
            {'href': 'home', 'name': 'домой'},
            {'href': 'products:index', 'name': 'продукты'},
            {'href': 'contact', 'name': 'контакты'}
               ]

    data = [
        {'title': 'Магазин'},
        {'main_menu': main_menu},

    ]
    products = Product.objects.all()[0:4]

    return render(request, 'mainapp/index.html', {
        'data': data,
        'products': products,
    })


def products(request, pk=None):
    print(pk)
    main_menu = [
            {'href': 'home', 'name': 'домой'},
            {'href': 'products:index', 'name': 'продукты'},
            {'href': 'contact', 'name': 'контакты'}
               ]

    data = [
        {'title': 'Продукты'},
        {'main_menu': main_menu},
    ]
    return render(request, 'mainapp/products.html', {
                      'data': data,
                  })


def contact(request):
    main_menu = [
        {'href': 'home', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'}
    ]

    data = [
        {'title': 'Контакты'},
        {'main_menu': main_menu},
    ]
    return render(request, 'mainapp/contact.html', {
        'data': data,
    })


def proba(request):
    prod = Product.objects.all()
    content = {'products': prod}
    return render(request, 'mainapp/proba.html', content)
