import django_filters
from .models import Products, Category


class ProductFilter(django_filters.FilterSet):
    # seller_id = django_filters.NumberFilter(lookup_expr='exact')
    brand = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    rank = django_filters.NumberFilter(lookup_expr='lt')
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
    )
    price= django_filters.NumericRangeFilter()

    class Meta:
        model = Products
        fields = ['brand', 'name', 'rank']
