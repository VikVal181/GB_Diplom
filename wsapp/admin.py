from django.contrib import admin
from .models import Type, Subtype, Product, DetailOrder, Order, Review


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    extra = 1


@admin.register(Subtype)
class SubtypeAdmin(admin.ModelAdmin):
    list_display = ('title_subt', 'type')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_pr', 'date_start', 'date_finish', 'difficulte', 'numbers', 'description_pr',  'type', 'subtype')


@admin.register(DetailOrder)
class DetailOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount_do', 'order', 'person')


class OrderHasDetailsInline(admin.TabularInline):
    model = DetailOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    inlines = [
        OrderHasDetailsInline,
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('mark', 'review', 'product', 'person')

