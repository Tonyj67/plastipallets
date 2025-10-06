# main/urls.py
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, ProductSitemap  # include ProductSitemap

# Define sitemaps for app-level access if needed (optional)
sitemaps = {
    'static': StaticSitemap,
    'products': ProductSitemap,  # Include dynamic products
}

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    
    # Individual product pages
    path('products/flat-top-hd/', views.flat_top_hd, name='flat_top_hd'),
    path('products/heavy-duty-grid/', views.heavy_duty_grid, name='heavy_duty_grid'),
    path('products/light-flat/', views.light_flat, name='light_flat'),
    path('products/light-grid/', views.light_grid, name='light_grid'),
    path('products/nestable/', views.nestable, name='nestable'),
    
    # All products page
    path('all-products/', views.all_products, name='all_products'),
    
    # Contact form email
    path('send-email/', views.send_email, name='send_email'),
    
    # Optional app-level sitemap (can be omitted if handled globally)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]













































































