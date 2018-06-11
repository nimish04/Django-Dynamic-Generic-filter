import django_filters
from .models import *


class PackageFilter(django_filters.FilterSet):
    # attributes = Product.objects.filter(attributes='color')
    # name = Product.objects.filter()

    class Meta:
        # model = ProductAttribute
        model = Package
        fields = ['name',]
