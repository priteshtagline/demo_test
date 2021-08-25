from django.contrib import admin

from coding_skill.models import MapHistory


@admin.register(MapHistory)
class MapHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'source_lat', 'source_long', 'destination_lat',
                    'destination_long', 'starting_place', 'ending_place', 'distance', 'created_date')
    list_display_links = ['user']
