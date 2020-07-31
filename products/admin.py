from django.contrib import admin
from .models import products, offer


class productsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class offerAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(offer, offerAdmin)
admin.site.register(products, productsAdmin)
