"""
URL configuration for plastipallets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# plastipallets/urls.py
"""
URL configuration for plastipallets project.
"""

# plastipallets/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap   # adjust if your sitemap is in a different app

# Django expects a dict of sitemaps
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', include('main.urls')),   # all your main app URLs
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

















