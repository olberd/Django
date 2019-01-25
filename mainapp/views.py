from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def main(request):

    main_menu = [
            {'href': 'home', 'name': 'домой'},
            {'href': 'products', 'name': 'продукты'},
            {'href': 'contact', 'name': 'контакты'}
               ]

    data = [
        {'title': 'Магазин'},
        {'main_menu': main_menu},
    ]

    return render(request, 'mainapp/index.html', {
        'data': data
    })


def products(request, id=0):
    main_menu = [
            {'href': 'home', 'name': 'домой'},
            {'href': 'products', 'name': 'продукты'},
            {'href': 'contact', 'name': 'контакты'}
               ]

    data = [
        {'title': 'Продукты'},
        {'main_menu': main_menu},
    ]
    return render(request, 'mainapp/products.html', {
                      'product_id': id,
                       'data': data,
                  })


def contact(request):
    main_menu = [
        {'href': 'home', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'}
    ]

    data = [
        {'title': 'Продукты'},
        {'main_menu': main_menu},
    ]
    return render(request, 'mainapp/contact.html', {
        'data': data,
    })
