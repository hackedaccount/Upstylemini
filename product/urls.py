from django.urls import path
from product import views
from django_filters.views import FilterView
from .filters import ProductFilter

app_name = 'product'
urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('upload_csv', views.profile_upload, name="upload_csv"),
    path('search', views.product_list, name='search'),

]
