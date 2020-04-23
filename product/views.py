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
        next(io_string)
        for column in csv.reader(io_string, delimiter=','):

            try:
                image_link = column[1].split(";")[0]
            except AttributeError:
                image_link = column[1]

            # price = float(re.sub("[^0-9^.]", "", column[10]))
            product_link = "https://www.amazon.co.uk/dp/" + str(column[94])
            asin = models.Products.objects.create(
                seller_id=str(column[53]),
                price=str(column[13]),
                name=str(column[2]),
                brand=str(column[102]),
                product_link=str(product_link),
                datetime=str(column[8]),
                rank=float(column[3]) if column[3] else None,
                ratings=float(column[6]) if column[6] else None,
                reviews=str(column[7]),
                asin=str(column[94]),
                image_link=str(image_link),
                category=str(column[91]),
            )
            # print(column[2])
            asin.save()
        return render(request, template)

    if 'toys' in request.FILES:
        # let's check if it is a csv file
        csv_file = request.FILES['toys']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream

        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=','):

            try:
                image_link = column[1].split(";")[0]
            except AttributeError:
                image_link = column[1]

            # price = float(re.sub("[^0-9^.]", "", column[10]))
            product_link = "https://www.amazon.co.uk/dp/" + str(column[71])
            asin = models.Products.objects.create(
                seller_id=str(column[42]),
                price=str(column[11]),
                name=str(column[2]),
                brand=str(column[79]),
                product_link=str(product_link),
                datetime=str(column[7]),
                rank=float(column[3]) if column[3] else None,
                ratings=float(column[5]) if column[5] else None,
                reviews=str(column[6]),
                asin=str(column[71]),
                image_link=str(image_link),
                category=str(column[68]),
            )
            print(column[2])
            asin.save()
        return render(request, template)

    if 'grocery' in request.FILES:
        # let's check if it is a csv file
        csv_file = request.FILES['grocery']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream

        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=','):

            try:
                image_link = column[1].split(";")[0]
            except AttributeError:
                image_link = column[1]

            # price = float(re.sub("[^0-9^.]", "", column[10]))
            product_link = "https://www.amazon.co.uk/dp/" + str(column[70])
            asin = models.Products.objects.create(
                seller_id=str(column[41]),
                price=str(column[10]) if str(column[10]) else str(column[7]),
                name=str(column[2]),
                brand=str(column[78]),
                product_link=str(product_link),
                datetime=str(column[6]),
                rank=float(column[3]) if column[3] else None,
                ratings=float(column[4]) if column[4] else None,
                reviews=str(column[5]),
                asin=str(column[70]),
                image_link=str(image_link),
                category=str(column[67]),
            )
            print(column[2])
            asin.save()
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

        category = models.Category.objects.get(pk=category_id).category if category_id else ''
        filtered_products = models.Products.objects.filter(name__icontains=name, brand__icontains=brand,
                                                           rank__lte=int(rank) if rank else 100000,
                                                           category__icontains=category).order_by(
            'rank') if name or brand or rank or category else models.Products.objects.all().order_by('rank')[:99]

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
