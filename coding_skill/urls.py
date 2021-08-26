from django.urls import path

from coding_skill.views import MapHistoryView

urlpatterns = [
    path('map-history/',
         MapHistoryView.as_view(), name='map_history'),
]
