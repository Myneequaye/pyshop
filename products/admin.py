from django.contrib import admin
from .models import Product, Offer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price', 'stock')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    '''Admin View for Offer'''

    list_display = ('code', 'discount')
    list_filter = ('code', 'discount')
    search_fields = ('code',)
    
