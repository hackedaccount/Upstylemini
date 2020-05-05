from django.contrib import admin
from tesco import models


# Register your models here.
@admin.register(models.TescoProducts)
class TescoProductsAdmin(admin.ModelAdmin):
    model = models.TescoProducts
