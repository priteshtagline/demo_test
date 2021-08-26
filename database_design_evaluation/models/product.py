# https://docs.djangoproject.com/en/3.2/topics/db/models/

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    """Store product realted details.
    """
    product_name = models.CharField(_("Product Name"), max_length=30)
    product_code = models.CharField(
        _("Product code"),
        max_length=255,
    )
    description = models.TextField(
        help_text=_("Detailed description."),
    )
    product_price = models.CharField(
        _("Product Price"),
        max_length=255,
    )

    class meta:
        # database modal name.
        db_table = "product"
        verbose_name = 'Product'

    def __str__(self):
        # return human related name.
        return self.product_name
