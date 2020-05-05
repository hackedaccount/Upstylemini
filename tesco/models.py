from django.db import models


# Create your models here.
class TescoProducts(models.Model):
    image_link = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)
    product_link = models.CharField(max_length=500, null=True, blank=True)
    product_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
