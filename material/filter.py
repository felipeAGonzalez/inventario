from django.db.models import Q, Value
from django.db.models.functions import Concat
from django_filters import rest_framework as filters

from .models import Material


class MaterialFilter(filters.FilterSet):
    """
    Material Filter.
    """

    search = filters.CharFilter(field_name="search", lookup_expr="icontains")
    order_by = filters.CharFilter(method="filter_order_by")

    def filter_order_by(self, queryset, name, value):
        """
        Order by filter.
        """
        if value.lower() == "desc":
            return queryset.order_by("-id")
        elif value.lower() == "asc":
            return queryset.order_by("id")
        else:
            return queryset

    class Meta:
        model = Material
        fields = {
            # "birth_date": ["exact", "lte", "gte", "lt", "gt"],
        }