from django.contrib import admin
from store_app.admin import ProductAdmin
from store_app.models import Product
from tags_app.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    extra = 0

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
