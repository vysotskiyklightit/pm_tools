from rest_framework import filters


class PathParamsFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filters_kwargs = {}
        current_field = ''

        field_names = list(view.kwargs)[-1:]
        for name in field_names:
            if current_field:
                current_field += f'__{name}'
            else:
                current_field = f'{name}'
            filters_kwargs.update({current_field: view.kwargs[name]})

        return queryset.filter(**filters_kwargs)
