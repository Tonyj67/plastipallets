from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from django.contrib.sites.models import Site
from django.conf import settings

# Import Product only if available
try:
    from .models import Product
    HAS_PRODUCTS = True
except (ImportError, Exception):
    HAS_PRODUCTS = False

# Get current site domain dynamically
try:
    CURRENT_DOMAIN = Site.objects.get_current().domain
    if not CURRENT_DOMAIN.startswith('http'):
        CURRENT_DOMAIN = 'https://' + CURRENT_DOMAIN
except:
    CURRENT_DOMAIN = getattr(settings, 'SITE_DOMAIN', 'https://www.plastipallets.com')

# -------------------------------
# Static Pages Sitemap (SEO Optimized)
# -------------------------------
class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        # Include ALL your valid URLs including individual product pages
        valid_urls = []
        url_candidates = [
            'home', 'about', 'products', 'contact', 'all_products',
            'flat_top_hd', 'heavy_duty_grid', 'light_flat', 
            'light_grid', 'nestable'
        ]
        
        for url_name in url_candidates:
            try:
                reverse(url_name)
                valid_urls.append(url_name)
            except:
                continue
        return valid_urls

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # Home page changes more frequently
        if item == 'home':
            return timezone.now()
        return None

    def priority(self, item):
        # Higher priority for important pages
        if item == 'home':
            return 1.0
        elif item in ['products', 'all_products']:
            return 0.9
        elif item in ['flat_top_hd', 'heavy_duty_grid', 'light_flat', 'light_grid', 'nestable']:
            return 0.8
        else:
            return 0.7

# -------------------------------
# Product Pages Sitemap (SEO Optimized)
# -------------------------------
class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    protocol = 'https'
    limit = 5000

    def items(self):
        if not HAS_PRODUCTS:
            return []
        try:
            return Product.objects.filter(is_published=True).order_by('-updated_at', '-created_at')
        except Exception as e:
            print(f"Product sitemap error: {e}")
            return []

    def location(self, obj):
        try:
            if hasattr(obj, 'get_absolute_url'):
                url_path = obj.get_absolute_url()
                if url_path.startswith('http'):
                    return url_path
                else:
                    return url_path
            elif hasattr(obj, 'slug'):
                return reverse('product_detail', kwargs={'slug': obj.slug})
            else:
                return f"/products/{obj.id}/"
        except Exception as e:
            print(f"Location error for {obj}: {e}")
            return f"/products/{obj.id}/"

    def lastmod(self, obj):
        if hasattr(obj, 'updated_at') and obj.updated_at:
            return obj.updated_at
        elif hasattr(obj, 'created_at') and obj.created_at:
            return obj.created_at
        else:
            return timezone.now()

# -------------------------------
# Sitemap Configuration
# -------------------------------
sitemaps = {
    'static': StaticSitemap,
}

# Conditionally add product sitemap
if HAS_PRODUCTS:
    try:
        test_products = Product.objects.exists()
        if test_products:
            sitemaps['products'] = ProductSitemap
    except:
        pass