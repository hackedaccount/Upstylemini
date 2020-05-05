from django.urls import path
from tesco import views

app_name = 'tesco'
urlpatterns = [
    path('', views.TescoProductList.as_view(), name='product_list'),
    path('upload_csv', views.tesco_product_upload, name="upload_csv"),
    path('search', views.tesco_product_list, name='search'),

]
