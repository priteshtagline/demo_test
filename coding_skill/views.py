import json
from collections import namedtuple

from django.db.models import Count, Q
from django.views.generic import ListView

from coding_skill.models import MapHistory

# Declaring namedtuple()


class MapHistoryView(ListView):
    """Website browse product list page

    Args:
        ListView ([Django Method]): [Extend by django generic listview]

    Returns:
        [html/text]: [return render html for browse product page]
    """
    model = MapHistory
    template_name = 'map_history.html'
    context_object_name = 'map_historys'
    # paginate_by = 40
    search_filter_data = {}

    def get_queryset(self):
        """Override django generic listview get_queryset method because
           as per requrments to diaplay product data by department, category and sub category so,
           pass keyword arguments to the url and hear filter by given keywords arguments.

           If user more product filter by brand, store and color then pass in query parameter and
           hear filter product by given querystring parameter.

        Returns:
            [queryset object]: [filter product queryset object data]
        """

        filter_fields = ('distance', 'created_date',
                         'starting_place', 'ending_place')

    
        query_dict = Q()
        data = json.loads(json.dumps(self.request.GET))
        for param in data:
            query_dict_set = Q()
            if param in filter_fields and self.request.GET.get(param):
                for key, value in eval(data[param]).items():
                    condition_field = '{0}__{1}'.format(param, key)
                    kwargs = {condition_field: value}
                    query_dict_set |= Q(**kwargs)
            query_dict &= query_dict_set
     
        print(query_dict)
        return super().get_queryset().filter(query_dict)


