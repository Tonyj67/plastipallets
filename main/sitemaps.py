# main/sitemap.py
from typing import List
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
# Ensure Product model exists in main/models.py or update the import path accordingly
# Example if Product is in main/products/models.py:
# from products.models import Product

from .models import Product  # Update this line if Product is not in main/models.py
from django.utils import timezone

BASE_URL = "https://www.plastipallets.com"

# -------------------------------
# Static Pages Sitemap
# -------------------------------
class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self) -> List[str]:
        return ['home', 'about', 'products', 'contact', 'all_products']

    def location(self, item: str) -> str:
        return f"{reverse(item)}"

    def lastmod(self, item: str):
        # Use current time or optionally track last updated date in your models
        return timezone.now()


# -------------------------------
# Product Pages Sitemap
# -------------------------------
class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.filter(is_published=True)

    def location(self, obj):
        return f"{BASE_URL}{obj.get_absolute_url()}"

    def lastmod(self, obj):
        # Automatically pick the product's last updated timestamp
        return obj.updated_at if hasattr(obj, 'updated_at') else timezone.now()
