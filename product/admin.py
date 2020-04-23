from django.contrib import admin
from product import models


# Register your models here.
@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    model = models.Products


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    model = models.Category


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    model = models.Brand
