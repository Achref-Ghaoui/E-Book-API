import django_filters
from .models import Book 


class ProductFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='iexact')
    keyword=django_filters.CharFilter(field_name="titre",lookup_expr="icontains")
    minPrice=django_filters.NumberFilter(field_name="price" or 0,lookup_expr="gte")
    maxPrice=django_filters.NumberFilter(field_name="price" or 100000,lookup_expr="lte")

    class Meta :
        model=Book
        fields=['titre','description','keyword','minPrice','maxPrice']