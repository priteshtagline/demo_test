from django.urls import path

from map_history.views import MapHistoryView

urlpatterns = [
    path('map-history/',
         MapHistoryView.as_view(), name='map_history'),
]
