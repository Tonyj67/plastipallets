# main/sitemap.py or plastipallets/sitemap.py
from typing import List   
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self) -> List[str]:
        return ['home', 'about', 'products', 'contact']
    
    def location(self, obj: str) -> str:
        return reverse(obj)







