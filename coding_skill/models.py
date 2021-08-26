from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class MapHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_lat = models.DecimalField(max_digits=9, decimal_places=6)
    source_long = models.DecimalField(max_digits=9, decimal_places=6)
    destination_lat = models.DecimalField(max_digits=9, decimal_places=6)
    destination_long = models.DecimalField(max_digits=9, decimal_places=6)
    starting_place = models.CharField(max_length=255)
    ending_place = models.CharField(max_length=255)
    distance = models.DecimalField(max_digits=9, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'map_history'
        verbose_name = _("Map History")
        verbose_name_plural = _("Map Historys")

    def __str__(self):
        return self.user.first_name
