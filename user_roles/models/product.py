# https://docs.djangoproject.com/en/3.2/topics/db/models/

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    """Store product realted details.
    """
    name = models.CharField(_("Name"), max_length=30)
    code = models.CharField(
        _("Code"),
        max_length=255,
    )
    description = models.TextField(
        help_text=_("Description"),
    )
    price = models.CharField(
        _("Price"),
        max_length=255,
    )

    class meta:
        # database modal name.
        db_table = "product"
        verbose_name = 'Product'

    def __str__(self):
        # return human related name.
        return self.name
