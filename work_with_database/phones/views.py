from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        all_obj = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        all_obj = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        all_obj = Phone.objects.all().order_by('-price')
    else:
        all_obj = Phone.objects.all()

    template = 'catalog.html'
    context = {
        'phones': all_obj
    }
    return render(request, template, context)



def show_product(request, slug):
    fil_obj = Phone.objects.get(slug = slug)
    template = 'product.html'
    context = {
        'phone': fil_obj
    }
    return render(request, template, context)

