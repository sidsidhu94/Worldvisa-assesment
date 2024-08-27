from django.db import models
from django.utils.translation import gettext_lazy as _
from categories.models import Category

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(
        _("Product name"),
        max_length=150,
        unique=True,
        help_text=_("This will be displayed to user as-is"),
    )
    description = models.TextField(
        _("descriptive write-up"),
        unique=False,
        help_text=_("Few sentences that showcase the appeal of the product"),
    )
    selling_price = models.DecimalField(
        _("price"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        related_name="products",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name} "

    class Meta:

        db_table = "product"
        ordering = []
        verbose_name = "Product"
        verbose_name_plural = "Products"