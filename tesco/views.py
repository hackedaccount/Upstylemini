from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views import generic
from tesco import models
import csv
import io
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tesco.filters import TescoProductFilter


# Create your views here.
class TescoProductList(LoginRequiredMixin, generic.ListView):
    template_name = 'tesco/tesco_products.html'
    context_object_name = 'tesco_products'
    paginate_by = 30

    def get_queryset(self):
        result = models.TescoProducts.objects.all()
        return result

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductList, self).get_context_data()
    #
    #     context["categories"] = models.Category.objects.all()
    #     context["brands"] = models.Brand.objects.all()
    #
    #     return context


def tesco_product_upload(request):
    template_name = 'tesco/tesco_csv_upload.html'
    if request.method == "GET":
        return render(request, template_name)

    if 'tesco' in request.FILES:
        # let's check if it is a csv file
        csv_file = request.FILES['tesco']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')

        # setup a stream which is when we loop through each line we are able to handle a data in a stream

        io_string = io.StringIO(data_set)
        # next(io_string)
        str_headers = next(io_string)
        # print(headers)
        headers = str_headers.replace(', ', ' ').replace('"', '').replace('\ufeff', '').replace('\r\n', '').split(',')
        column_name = headers.index('name')
        column_price = headers.index('price')
        column_product_link = headers.index('product_link')
        column_product_id = headers.index('id')

        for column in csv.reader(io_string, delimiter=','):
            image_id = int(column[column_product_id]) % 1000
            image_link = 'https://img.tesco.com/Groceries/pi/{}/{}/IDShot_225x225.jpg'.format(image_id,
                                                                                              column[column_product_id])
            product_link = 'https://www.tesco.com{}'.format(column[column_product_link])
            tesco, created = models.TescoProducts.objects.update_or_create(product_id=int(column[column_product_id]),
                                                                           defaults={
                                                                               'name': column[column_name],
                                                                               'price': column[column_price],
                                                                               'product_link': product_link,
                                                                               'image_link': image_link,
                                                                           })
            print('name:{},price{},{}'.format(tesco.name, tesco.price, tesco.image_link))

        return render(request, template_name)


def tesco_product_list(request):
    f = TescoProductFilter(request.GET)
    context = {'filter': f}
    # filter_data = f.data

    if f.is_valid():
        context = {'filter': f}
        name = request.GET.get('name', '')

        filtered_products = models.TescoProducts.objects.filter(name__icontains=name) if name else models.TescoProducts.objects.all()[:30]

        page = request.GET.get('page', 1)

        paginator = Paginator(filtered_products, 30)

        try:
            filtered_products = paginator.page(page)
        except PageNotAnInteger:
            filtered_products = Paginator.page(1)
        except EmptyPage:
            filtered_products = paginator.page(paginator.num_pages)

        context['page_obj'] = filtered_products

    else:
        f = TescoProductFilter()
        context = {'filter': f}
    return render(request, 'tesco/tesco_filter.html', context)
