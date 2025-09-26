# main/sitemap.py or plastipallets/sitemap.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'products', 'contact']
    
    def location(self, item):
        return reverse(item)






