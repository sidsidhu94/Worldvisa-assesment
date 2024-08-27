from django.contrib import admin
from products.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category")  
    ordering = ("-id",)
    search_fields = ("product_name",)  
    list_filter = ("category",)
    fields = (
        ("product_name", "category"),
        "description",
        ("id", "created_at", "edited_at"),
    )
    autocomplete_fields = ("category",)
    readonly_fields = ("id", "created_at", "edited_at")