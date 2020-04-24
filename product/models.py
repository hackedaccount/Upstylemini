from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.category


class Brand(models.Model):
    brand = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.brand


class Products(models.Model):
    seller_id = models.CharField(max_length=500, null=True, blank=True)
    asin = models.CharField(primary_key=True, max_length=500)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    datetime = models.CharField(max_length=500, null=True, blank=True)
    image_link = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)
    product_link = models.CharField(max_length=500, null=True, blank=True)
    rank = models.IntegerField(null=True)
    reviews = models.CharField(max_length=500, null=True, blank=True)
    ratings = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Asins(models.Model):
    asin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.asin
