from django.shortcuts import render
from django.views import generic
from comparison.filters import ComparisonFilter
from product.models import Products
from tesco.models import TescoProducts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def comparison_list(request):
    template = "comparison/comparison.html"
    f = ComparisonFilter(request.GET)
    context = {'filter': f}
    # filter_data = f.data

    if f.is_valid():
        context = {'filter': f}
        name = request.GET.get('name', '')

        filtered_amazon_products = Products.objects.filter(name__icontains=name)
        filtered_tesco_products = TescoProducts.objects.filter(name__icontains=name)
        filtered_products = []
        t_list = len(filtered_tesco_products)
        a_list = len(filtered_amazon_products)
        length = t_list if t_list <= a_list else a_list
        for i in range(length):
            filtered_products.append(filtered_amazon_products[i])
            filtered_products.append(filtered_tesco_products[i])


        page = request.GET.get('page', 1)
        paginator = Paginator(filtered_products, 10)
        # amazon pagination
        try:
            filtered_products = paginator.page(page)
        except PageNotAnInteger:
            filtered_products = paginator.page(1)
        except EmptyPage:
            filtered_products = paginator.page(paginator.num_pages)

        # context['filtered_amazon_products'] = filtered_amazon_products
        context['filtered_products'] = filtered_products

        # tesco pagination
        # tesco_products_paginator = Paginator(filtered_tesco_products, 100)[:5]
        #
        # try:
        #     filtered_tesco_products = tesco_products_paginator.page(page)
        # except PageNotAnInteger:
        #     filtered_tesco_products = tesco_products_paginator.page(1)
        # except EmptyPage:
        #     filtered_tesco_products = tesco_products_paginator.page(tesco_products_paginator.num_pages)

        # context['filtered_tesco_products'] = filtered_tesco_products

    else:
        f = ComparisonFilter()
        context = {'filter': f}
    return render(request, template, context)
