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
    asin = models.CharField(max_length=500, null=True, blank=True)
    brand = models.CharField(max_length=500, null=True, blank=True)
    datetime = models.CharField(max_length=500, null=True, blank=True)
    image_link = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)
    product_link = models.CharField(max_length=500, null=True, blank=True)
    rank = models.IntegerField(null=True)
    reviews = models.CharField(max_length=500, null=True, blank=True)
    ratings = models.IntegerField(null=True)
    category = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Asins(models.Model):
    asin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.asin


class ProductsKeepa(models.Model):
    locale = models.CharField(max_length=500, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    sales_rank_current = models.CharField(max_length=500, null=True, blank=True)
    reviews_rating = models.CharField(max_length=500, null=True, blank=True)
    reviews_review_count = models.CharField(max_length=500, null=True, blank=True)
    last_price_change = models.CharField(max_length=500, null=True, blank=True)
    amazon_current = models.CharField(max_length=500, null=True, blank=True)
    amazon_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    amazon_out_of_stock_percentage_90_days_oos = models.CharField(max_length=500, null=True, blank=True)
    new_current = models.CharField(max_length=500, null=True, blank=True)
    new_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    new_3_rd_party_fba_current = models.CharField(max_length=500, null=True, blank=True)
    new_3_rd_party_fba_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    fba_fees = models.CharField(max_length=500, null=True, blank=True)
    new_3_rd_party_fbm_current = models.CharField(max_length=500, null=True, blank=True)
    new_3_rd_party_fbm_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    used_current = models.CharField(max_length=500, null=True, blank=True)
    used_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    list_price_current = models.CharField(max_length=500, null=True, blank=True)
    list_price_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    lightning_deals_current = models.CharField(max_length=500, null=True, blank=True)
    lightning_deals_upcoming_deal = models.CharField(max_length=500, null=True, blank=True)
    warehouse_deals_current = models.CharField(max_length=500, null=True, blank=True)
    warehouse_deals_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    collectible_current = models.CharField(max_length=500, null=True, blank=True)
    collectible_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    refurbished_current = models.CharField(max_length=500, null=True, blank=True)
    refurbished_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    new_offer_count_current = models.CharField(max_length=500, null=True, blank=True)
    new_offer_count_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    count_of_retrieved_live_offers_new_fba = models.CharField(max_length=500, null=True, blank=True)
    count_of_retrieved_live_offers_new_fbm = models.CharField(max_length=500, null=True, blank=True)
    used_offer_count_current = models.CharField(max_length=500, null=True, blank=True)
    used_offer_count_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    refurbished_offer_count_current = models.CharField(max_length=500, null=True, blank=True)
    refurbished_offer_count_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    collectible_offer_count_current = models.CharField(max_length=500, null=True, blank=True)
    collectible_offer_count_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    buy_box_current = models.CharField(max_length=500, null=True, blank=True)
    buy_box_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    buy_box_seller = models.CharField(max_length=500, null=True, blank=True)
    used_like_new_current = models.CharField(max_length=500, null=True, blank=True)
    used_like_new_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    used_very_good_current = models.CharField(max_length=500, null=True, blank=True)
    used_very_good_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    used_good_current = models.CharField(max_length=500, null=True, blank=True)
    used_good_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    used_acceptable_current = models.CharField(max_length=500, null=True, blank=True)
    used_acceptable_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    collectible_like_new_current = models.CharField(max_length=500, null=True, blank=True)
    collectible_like_new_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    collectible_very_good_current = models.CharField(max_length=500, null=True, blank=True)
    collectible_very_good_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    collectible_good_current = models.CharField(max_length=500, null=True, blank=True)
    collectible_good_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    collectible_acceptable_current = models.CharField(max_length=500, null=True, blank=True)
    collectible_acceptable_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    refurbished_current_2 = models.CharField(max_length=500, null=True, blank=True)
    refurbished_90_days_avg_2 = models.CharField(max_length=500, null=True, blank=True)
    e_bay_new_current = models.CharField(max_length=500, null=True, blank=True)
    e_bay_new_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    e_bay_used_current = models.CharField(max_length=500, null=True, blank=True)
    e_bay_used_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    trade_in_current = models.CharField(max_length=500, null=True, blank=True)
    trade_in_90_days_avg = models.CharField(max_length=500, null=True, blank=True)
    tracking_since = models.CharField(max_length=500, null=True, blank=True)
    categories_root = models.CharField(max_length=500, null=True, blank=True)
    categories_sub = models.CharField(max_length=500, null=True, blank=True)
    categories_tree = models.CharField(max_length=500, null=True, blank=True)
    asin = models.CharField(max_length=500, null=True, blank=True)
    product_codes_ean = models.CharField(max_length=500, null=True, blank=True)
    product_codes_upc = models.CharField(max_length=500, null=True, blank=True)
    product_codes_part_number = models.CharField(max_length=500, null=True, blank=True)
    parent_asin = models.CharField(max_length=500, null=True, blank=True)
    variation_asins = models.CharField(max_length=500, null=True, blank=True)
    freq_bought_together = models.CharField(max_length=500, null=True, blank=True)
    manufacturer = models.CharField(max_length=500, null=True, blank=True)
    brand = models.CharField(max_length=500, null=True, blank=True)
    product_group = models.CharField(max_length=500, null=True, blank=True)
    model = models.CharField(max_length=500, null=True, blank=True)
    color = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=500, null=True, blank=True)
    edition = models.CharField(max_length=500, null=True, blank=True)
    format = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=500, null=True, blank=True)
    binding = models.CharField(max_length=500, null=True, blank=True)
    number_of_items = models.CharField(max_length=500, null=True, blank=True)
    number_of_pages = models.CharField(max_length=500, null=True, blank=True)
    publication_date = models.CharField(max_length=500, null=True, blank=True)
    release_date = models.CharField(max_length=500, null=True, blank=True)
    languages = models.CharField(max_length=500, null=True, blank=True)
    package_dimension_cm = models.CharField(max_length=500, null=True, blank=True)
    package_weight_g = models.CharField(max_length=500, null=True, blank=True)
    item_dimension_cm = models.CharField(max_length=500, null=True, blank=True)
    item_weight_g = models.CharField(max_length=500, null=True, blank=True)
    adult_product = models.CharField(max_length=500, null=True, blank=True)
    trade_in_eligible = models.CharField(max_length=500, null=True, blank=True)
    prime_eligible_amazon_offer = models.CharField(max_length=500, null=True, blank=True)
    subscribe_and_save = models.CharField(max_length=500, null=True, blank=True)
    one_time_coupon_absolute = models.CharField(max_length=500, null=True, blank=True)
    one_time = models.CharField(max_length=500, null=True, blank=True)
    coupon_percentage = models.CharField(max_length=500, null=True, blank=True)
    subscribe_and_save_coupon_percentage = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return ' - '.join([str(self.title), str(self.asin)])
