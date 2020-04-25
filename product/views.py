from django.shortcuts import render
from product import models
import csv
import io
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views import generic
from tablib import Dataset
from . import filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from .filters import ProductFilter


# Create your views here.

class ProductList(LoginRequiredMixin, generic.ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        result = models.Products.objects.all().order_by('rank')
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data()

        context["categories"] = models.Category.objects.all()
        context["brands"] = models.Brand.objects.all()

        return context


def profile_upload(request):
    # declaring template
    template = "csv_upload.html"
    data = models.Products.objects.last()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    if 'beauty' in request.FILES:
        # let's check if it is a csv file
        csv_file = request.FILES['beauty']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')

        # setup a stream which is when we loop through each line we are able to handle a data in a stream

        io_string = io.StringIO(data_set)
        # next(io_string)
        str_headers = next(io_string)
        # print(headers)
        headers = str_headers.replace(', ', ' ').replace('"', '').replace('\ufeff', '').split(',')
        image_column = headers.index('Image')
        title_column = headers.index('Title')
        rank_column = headers.index('Sales Rank: Current')
        ratings_column = headers.index('Reviews: Rating')
        reviews_column = headers.index('Reviews: Review Count')
        last_price_change_column = headers.index('Last Price Change')
        price_column = headers.index('New: Current')
        seller_column = headers.index('Buy Box Seller')
        category_column = headers.index('Categories: Root')
        asin_column = headers.index('ASIN')
        brand_column = headers.index('Brand')

        for column in csv.reader(io_string, delimiter=','):

            try:
                image_link = column[image_column].split(";")[0]
            except AttributeError:
                image_link = column[image_column]
            category, created = models.Category.objects.get_or_create(category=str(column[category_column]))
            # print(created, end=' ')

            brand, created = models.Brand.objects.get_or_create(brand=str(column[brand_column]))
            # print(created, end=' ')

            # price = float(re.sub("[^0-9^.]", "", column[10]))
            product_link = "https://www.amazon.co.uk/dp/" + str(column[asin_column])
            asin, created = models.Products.objects.update_or_create(asin=str(column[asin_column]), defaults={
                'seller_id': str(column[seller_column]),
                'price': str(column[price_column]),
                'name': str(column[title_column]),
                'brand': brand,
                'product_link': str(product_link),
                'datetime': str(column[last_price_change_column]),
                'rank': int(column[rank_column]) if column[rank_column] else None,
                'ratings': str(column[ratings_column]),
                'reviews': str(column[reviews_column]),
                'image_link': str(image_link),
                'category': category,
            })
            # print('asin:{},category{},{}'.format(asin.asin, asin.category, str(created)))

        return render(request, template)


def product_list(request):
    f = ProductFilter(request.GET)
    context = {'filter': f}
    # filter_data = f.data

    if f.is_valid():
        context = {'filter': f}
        name = request.GET.get('name', '')
        brand = request.GET.get('brand', '')
        rank = request.GET.get('rank', '')
        category_id = request.GET.get('category', '')

        filtered_products = models.Products.objects.filter(name__icontains=name, brand__brand__icontains=brand,
                                                           rank__lte=int(rank) if rank else 100000, ).order_by(
            'rank') if name or rank or category_id or brand else models.Products.objects.all().order_by('rank')[:99]

        if category_id:
            category = models.Category.objects.get(pk=category_id)
            filtered_products = filtered_products.filter(category=category)
        #
        # if brand_id:
        #     brand = models.Brand.objects.get(brand__icontains=brand_id)
        #     filtered_products = filtered_products.filter(brand=brand)

        page = request.GET.get('page', 1)

        paginator = Paginator(filtered_products, 100)

        try:
            filtered_products = paginator.page(page)
        except PageNotAnInteger:
            filtered_products = Paginator.page(1)
        except EmptyPage:
            filtered_products = paginator.page(paginator.num_pages)

        context['page_obj'] = filtered_products

    else:
        f = ProductFilter()
        context = {'filter': f}
    return render(request, 'filter.html', context)
