import django_filters
from tesco.models import TescoProducts


class TescoProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TescoProducts
        fields = ['name']
