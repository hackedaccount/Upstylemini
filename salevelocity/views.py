from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from salevelocity import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from salevelocity.forms import SaleVelocityForm
import csv
import io
import re
import datetime
from django.utils import timezone
import pytz
import tablib


# Create your views here.
def find_int_vale(text):
    text = text.split('.')
    whole = re.findall(r'[0-9]+', text[0])
    whole = ''.join(whole)
    try:
        decimal = re.findall(r'[0-9]+', text[1])
        decimal = ''.join(decimal)
    except:
        decimal = '0'
    final_value = '.'.join([whole, decimal])
    return float(final_value)


def salevelocity_upload(request):
    # declaring template
    template = "salevelocity/csv_upload.html"

    if request.method == "GET":
        return render(request, template)

    if 'salevelocity' in request.FILES:
        # let's check if it is a csv file
        csv_file = request.FILES['salevelocity']
        days = find_int_vale(request.POST.get('days', ''))

        if not csv_file.name.endswith('.csv'):
            return render(request, template, {'message': 'Not a CSV FILE'})
        data_set = csv_file.read().decode('UTF-8')

        # setup a stream which is when we loop through each line we are able to handle a data in a stream

        io_string = io.StringIO(data_set)
        # next(io_string)
        str_headers = next(io_string)
        # print(headers)
        headers = str_headers.replace(', ', ' ').replace('"', '').replace('\ufeff', '').split(',')
        asin = headers.index('(Parent) ASIN')
        title = headers.index('Title')
        sessions = headers.index('Sessions')
        session_percentage = headers.index('Session Percentage')
        page_views = headers.index('Page Views')
        page_views_percentage = headers.index('Page Views Percentage')
        buy_box_percentage = headers.index('Buy Box Percentage')
        units_ordered = headers.index('Units Ordered')
        units_ordered_b2b = headers.index('Units Ordered – B2B')
        unit_session_percentage = headers.index('Unit Session Percentage')
        unit_session_percentage_b2b = headers.index('Unit Session Percentage – B2B')
        ordered_product_sales = headers.index('Ordered Product Sales')
        ordered_product_sales_b2b = headers.index('Ordered Product Sales – B2B')
        total_order_items = headers.index('Total Order Items')
        total_order_items_b2b = headers.index('Total Order Items – B2B')

        for column in csv.reader(io_string, delimiter=','):
            average_selling_price = (find_int_vale(column[ordered_product_sales]) + find_int_vale(
                column[ordered_product_sales_b2b])) / (find_int_vale(column[total_order_items]) + find_int_vale(
                column[total_order_items_b2b]))
            sales_velocity = (find_int_vale(column[buy_box_percentage]) * find_int_vale(
                column[sessions]) * average_selling_price) / days / 100
            object = models.SaleVelocity.objects.create(asin=column[asin],
                                                        title=column[title],
                                                        sessions=find_int_vale(column[sessions]),
                                                        session_percentage=find_int_vale(
                                                            column[session_percentage]) / 100,
                                                        page_views=find_int_vale(column[page_views]),
                                                        page_views_percentage=find_int_vale(
                                                            column[page_views_percentage]) / 100,
                                                        buy_box_percentage=find_int_vale(
                                                            column[buy_box_percentage]),
                                                        units_ordered=find_int_vale(column[units_ordered]),
                                                        units_ordered_b2b=find_int_vale(
                                                            column[units_ordered_b2b]),
                                                        unit_session_percentage=find_int_vale(
                                                            column[unit_session_percentage]) / 100,
                                                        unit_session_percentage_b2b=find_int_vale(
                                                            column[unit_session_percentage_b2b]) / 100,
                                                        ordered_product_sales=find_int_vale(
                                                            column[ordered_product_sales]),
                                                        ordered_product_sales_b2b=find_int_vale(
                                                            column[ordered_product_sales_b2b]),
                                                        total_order_items=find_int_vale(
                                                            column[total_order_items]),
                                                        total_order_items_b2b=find_int_vale(
                                                            column[total_order_items_b2b]),
                                                        average_selling_price=average_selling_price,
                                                        sales_velocity=sales_velocity,
                                                        days=days,
                                                        datetime=datetime.datetime.now(tz=timezone.utc)
                                                        )
            # print('average_selling_price:{},    sales_velocity{}'.format(object.average_selling_price,
            #                                                              object.sales_velocity))

        return render(request, template)


class HistoryData(LoginRequiredMixin, generic.FormView):
    template_name = 'salevelocity/history_data.html'

    form_class = SaleVelocityForm

    def get(self, request, *args, **kwargs):

        form = SaleVelocityForm(request.GET)

        print(form.errors)
        if form.is_valid():
            context = {'form': form}
            start_date_year = request.GET.get('start_date_year', '')
            start_date_month = request.GET.get('start_date_month', '')
            start_date_day = request.GET.get('start_date_day', '')
            end_date_year = request.GET.get('end_date_year', '')
            end_date_month = request.GET.get('end_date_month', '')
            end_date_day = request.GET.get('end_date_day', '')
            start_date = datetime.date(int(start_date_year), int(start_date_month), int(start_date_day))
            end_date = datetime.date(int(end_date_year), int(end_date_month), int(end_date_day))
            download = request.GET.get('download', '')

            salevelocity = models.SaleVelocity.objects.filter(datetime__range=(start_date, end_date))
            if download == 'on':
                headers = ('Timestamp', '(Parent) ASIN', 'Title', 'Sessions', 'Session Percentage', 'Page Views',
                           'Page Views Percentage', 'Buy Box Percentage', 'Units Ordered', 'Units Ordered – B2B',
                           'Unit Session Percentage', 'Unit Session Percentage – B2B', 'Ordered Product Sales',
                           'Ordered Product Sales – B2B', 'Total Order Items', 'Total Order Items – B2B',
                           'AverageSelling price', 'Sales Velocity based on 45 days sales', 'Days')
                response_data = tablib.Dataset(headers=headers)
                for item in salevelocity.all():
                    response_data.append(
                        [item.datetime.astimezone(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'),
                         item.asin, item.title, item.sessions, item.session_percentage, item.page_views,
                         item.page_views_percentage, item.buy_box_percentage, item.units_ordered,
                         item.units_ordered_b2b, item.unit_session_percentage, item.unit_session_percentage_b2b,
                         item.ordered_product_sales, item.ordered_product_sales_b2b, item.total_order_items,
                         item.total_order_items_b2b, item.average_selling_price, item.sales_velocity, item.days])
                response = HttpResponse(content_type='text/csv')
                response[
                    'Content-Disposition'] = 'attachment; filename="salevelocity_{date}.csv"'.format(
                    date=datetime.datetime.now().strftime('%Y_%m_%d'))
                response.write(response_data.export('csv'))
                return response
            else:
                page = request.GET.get('page', 1)
                paginator = Paginator(salevelocity, 50)

                try:
                    salevelocity = paginator.page(page)
                except PageNotAnInteger:
                    salevelocity = Paginator.page(paginator.num_pages)
                except EmptyPage:
                    salevelocity = paginator.page(paginator.num_pages)

                context['salevelocity'] = salevelocity

            return render(request, self.template_name, context)
        else:
            form = SaleVelocityForm()
            context = {'form': form}
        return render(request, self.template_name, context)
