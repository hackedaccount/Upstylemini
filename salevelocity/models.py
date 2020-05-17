from django.db import models


# Create your models here.
class SaleVelocity(models.Model):
    asin = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    sessions = models.IntegerField()
    session_percentage = models.DecimalField(max_digits=19, decimal_places=10)
    page_views = models.IntegerField()
    page_views_percentage = models.DecimalField(max_digits=19, decimal_places=10)
    buy_box_percentage = models.DecimalField(max_digits=19, decimal_places=10)
    units_ordered = models.IntegerField()
    units_ordered_b2b = models.IntegerField()
    unit_session_percentage = models.DecimalField(max_digits=19, decimal_places=10)
    unit_session_percentage_b2b = models.DecimalField(max_digits=19, decimal_places=10)
    ordered_product_sales = models.DecimalField(max_digits=19, decimal_places=10)
    ordered_product_sales_b2b = models.DecimalField(max_digits=19, decimal_places=10)
    total_order_items = models.IntegerField()
    total_order_items_b2b = models.IntegerField()
    average_selling_price = models.DecimalField(max_digits=19, decimal_places=10)
    sales_velocity = models.DecimalField(max_digits=19, decimal_places=10)
    days = models.IntegerField()
    datetime = models.DateTimeField(blank=True)

    def __str__(self):
        return '-'.join([self.asin, str(self.average_selling_price), str(self.sales_velocity), str(self.days)])

    class Meta:
        ordering = ['datetime', ]
