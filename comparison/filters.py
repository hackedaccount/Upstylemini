import django_filters
from product.models import Products


class ComparisonFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Products
        fields = ['name']
