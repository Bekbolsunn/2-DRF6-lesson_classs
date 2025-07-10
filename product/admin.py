from django.contrib import admin
from .models import Category, Product, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['title']
    list_filter = ['price', 'category']
    list_display = ['title', 'price', 'category']
    list_editable = ['price']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
