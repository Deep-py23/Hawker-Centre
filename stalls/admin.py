from django.contrib import admin

from .models import Category, Dish, Stall


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Stall)
class StallAdmin(admin.ModelAdmin):
    list_display = ('name', 'stall_number', 'owner', 'is_open')
    list_filter = ('is_open',)
    search_fields = ('name', 'stall_number')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'stall', 'category', 'price', 'is_available')
    list_filter = ('stall', 'category', 'is_available')
    search_fields = ('name',)