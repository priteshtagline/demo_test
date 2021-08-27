import json
from collections import namedtuple

from django.db.models import Count, Q
from django.views.generic import ListView

from coding_skill.models import MapHistory


class MapHistoryView(ListView):
    """Website map history fillter list page

    Args:
        ListView ([Django Method]): [Extend by django generic listview]

    Returns:
        [html/text]: [return render html for browse product page]
    """
    model = MapHistory
    template_name = 'map_history.html'
    context_object_name = 'map_historys'
    search_filter_data = {}

    def get_queryset(self):
        """Override django generic listview get_queryset method because
           as per requrments to display map history data fillter by distance, 
           starting place, enadig plasce and dreated Date so, pass keyword 
           arguments to the url and hear filter by given keywords arguments.

        Returns:
            [queryset object]: [filter map history queryset object data]
        """

        filter_fields = {
            "distance": ['lt', 'gt', 'eq', 'gte', 'lte'],
            "created_date": ['lt', 'gt', 'eq', 'gte', 'lte'],
            "starting_place": ['iexact'],
            "ending_place": ['iexact']
        }

        query_dict = Q()
        data = json.loads(json.dumps(self.request.GET))
        for param in data:
            query_dict_set = Q()
            if param in filter_fields.keys() and self.request.GET.get(param):
                for condition, value in eval(data[param]).items():
                    if condition in filter_fields[param]:
                        kwargs = {'{0}__{1}'.format(param, condition): value}
                        query_dict_set |= Q(**kwargs)
            query_dict &= query_dict_set

        return super().get_queryset().filter(query_dict)
