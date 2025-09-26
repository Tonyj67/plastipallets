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

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import sitemaps_dict   # adjust import if your file name differs

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),

    # All site pages live inside the 'main' app
    path("", include("main.urls")),

    # XML sitemap for search engines
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps_dict},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
