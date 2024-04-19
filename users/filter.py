from django.db.models import Q, Value
from django.db.models.functions import Concat
from django_filters import rest_framework as filters

from users.models import Users


class UserFilter(filters.FilterSet):
    """
    User Filter.
    """

    first_name = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    phone = filters.CharFilter(field_name="phone", lookup_expr="icontains")
    # search field is a custom filter that allows to search by first_name, last_name, email, phone and family__name
    search_field = filters.CharFilter(method="filter_search_field")

    # def filter_search_field(self, queryset, name, value):
    #     """
    #     Filter by search field.

    #     The filter is case insensitive, ignores accents (for spanish) and
    #     matches any part of the name.
    #     """
    #     queryset = queryset.annotate(
    #         full_name=Concat(
    #             "first_name",
    #             Value(" "),
    #             "last_name",
    #         )
    #     )
    #     return queryset.filter(
    #         Q(full_name__unaccent__icontains=value)
    #         | Q(user__email__unaccent__icontains=value)
    #         | Q(phone__unaccent__icontains=value)
    #         | Q(family__name__unaccent__icontains=value)
    #     )

    class Meta:
        model = Users
        fields = {
            # "birth_date": ["exact", "lte", "gte", "lt", "gt"],
        }
