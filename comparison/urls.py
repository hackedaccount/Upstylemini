from django.urls import path
from comparison import views

app_name = 'comparison'
urlpatterns = [

    path('compare', views.comparison_list, name='compare'),
]
