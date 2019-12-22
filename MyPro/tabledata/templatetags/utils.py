from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_item_from_queryset(queryset, key):
    return queryset.values_list(key, flat=True)[0]
