from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inverntory'
    parameter_name = 'inverntory'
    def lookups(self, request, model_admin):
        return [ ('<10', 'Low') ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {'slug': ['title']}
    exclude = ['promotions']
    actions = ['clear_inventory']
    list_display = [
        'title',
        'unit_price',
        'inventory_status',
        'collection_title'
    ]
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]
    search_fields = ['title']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        update_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{update_count} porducts were successfully updated.'
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['user__first_name', 'user__last_name']
    list_select_related = ['user']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']
    @admin.display(ordering='products_count')

    def products_count(slef, collection):
        url = (
            reverse('admin:store_app_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html(
            '<a href="{}">{}</a>', url, collection.products_count
        )

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )
