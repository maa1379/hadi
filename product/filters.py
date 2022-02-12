import django_filters
from .models import ProductBase, Loaded, InternalProduct, ExportalProduct


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = ProductBase
        fields = ['mine',
                  'stone_name',
                  'length',
                  'width',
                  'height',
                  'approximate_tonnage']


class LoadedFilter(django_filters.FilterSet):
    class Meta:
        model = Loaded
        fields = [
            'mine'
        ]


class DomesticFilter(django_filters.FilterSet):
    class Meta:
        model = InternalProduct
        fields = [
            'mine'
        ]


class ExportalFilter(django_filters.FilterSet):
    class Meta:
        model = ExportalProduct
        fields = [
            'mine'
        ]
