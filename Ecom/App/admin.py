from django.contrib import admin
from App.models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
    search_fields = ["category"]  # Required for `autocomplete_fields` in ProductAdmin

class DiamensionInline(admin.TabularInline):
    model = Dimensions
    extra = 0
    # extra = 3 Display three Diamension row.


@admin.register(Product)
class PrdouctAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "title",
        "price",
        "discount_percentage",
        "rating",
        "stock",
        "availabilityStatus",
        "sku"
    ]
    search_fields = (
        "category__category__icontains",
        "title",
        "price",
        "discount_percentage",
        "rating",
        "stock",
        "availabilityStatus",
        "sku"
    )
    search_fields = ['category__category',]
    autocomplete_fields = ['category',]
    exclude = ["price",]
    list_filter = ("availabilityStatus",)
    readonly_fields = ("sku","availabilityStatus")
    inlines = [DiamensionInline]

    actions = ["In_stock_availability_status","Out_of_stock_availability_status"]


    def In_stock_availability_status(self, request,queryset):
        queryset.update(availabilityStatus = "In Stock")
    In_stock_availability_status.short_description = "Mark as in Avilable Stock"


    def Out_of_stock_availability_status(self,requset,queryset):
        queryset.update(availabilityStatus = "Out of Stock")
    Out_of_stock_availability_status

@admin.register(Dimensions)
class DiamensionAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "width",
        "height",
        "depth"
    )
    #NOTE: if you can use the list into readonly fields so that the can modifying so if they give it one link 
    # readonly_fields = ["product"]
    # search_fields = (
    #     "product__title__icontains",
    #     "width",
    #     "height",
    #     "depth"
    # )
    # search_fields = ["product__title"]
    # autocomplete_fields = ["product__title"]

@admin.register(Images)

class ImageAdmin(admin.ModelAdmin):
    search_fields = (
        'product__title',  
    )
    list_display = [
       "product",
       "images"
    ]

admin.site.register(Thumbnail)
admin.site.register(CartItem)