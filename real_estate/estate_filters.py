from .models import RealEstate


def estate_filters(request):
    filters_dict = {}
    sort_by = 'created_at'
    order_by = request.GET.get('order', 'desc')
    sort_by = sort_by if order_by == 'asc' else f'-{sort_by}'
    filters = ['type_of_deal', 'city_district__city_district', 'metro__metro_station', 'floor__gte', 'rooms',
               'bathroom']
    for one_filter in filters:
        choice = request.GET.get(one_filter, '')
        if choice:
            if choice == '5_and_more':
                filters_dict[one_filter + '__gte'] = '5'
            else:
                filters_dict[one_filter] = choice
    estates = RealEstate.objects.order_by(sort_by).filter(**filters_dict)
    return estates
