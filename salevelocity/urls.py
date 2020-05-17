from django.urls import path
from salevelocity import views

app_name = 'salevelocity'
urlpatterns = [
    path('', views.salevelocity_upload, name='sale_velocity'),
    path('history_data', views.HistoryData.as_view(), name='history_data'),

    # path('error', views.handler404, name='error')

]
