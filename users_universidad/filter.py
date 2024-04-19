from django.db.models import Q, Value
from django.db.models.functions import Concat
from django_filters import rest_framework as filters

from .models import UsersUniversidad


class UsersUniversidadFilter(filters.FilterSet):
    """
    UsersUniversidad Filter.
    """

    search = filters.CharFilter(method="filter_search")
    order_by = filters.CharFilter(method="filter_order_by")

    def filter_search(self, queryset, name, value):
        """
        Search filter.
        """
        return queryset.filter(
            Q(user__name__icontains=value) |
            Q(universidad__name__icontains=value)
        )

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
        model = UsersUniversidad
        fields = {}
