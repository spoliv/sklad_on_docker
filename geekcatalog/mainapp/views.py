from mainapp.models import Product
from mainapp.forms import ProductForm
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse


def catalog_view(request):
    title = 'Домой'
    products = Product.objects.all()
    return render(request, 'mainapp/goods_list.html',
                  context={'title': title,
                           'products': products,
                           })


def add_prod(request):
    data = dict()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all()
            data['html_good_list'] = render_to_string('mainapp/products_table_part.html', {'products': products})
        else:
            data['form_is_valid'] = False
    form = ProductForm()
    context = {'product_form': form}
    data['html_form'] = render_to_string('mainapp/good_create.html', context, request=request)
    return JsonResponse(data)



# Create your views here.
