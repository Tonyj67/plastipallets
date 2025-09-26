from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Add any named URL patterns for static pages
        return [
            'home',
            'about',
            'products',
            'contact',
        ]

    def location(self, obj: str):
        return reverse(obj)
