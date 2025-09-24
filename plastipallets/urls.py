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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
    <h1>PlastiPallets is Working!</h1>
    <p>Your Django app is successfully deployed on Heroku!</p>
    <p><a href="/admin/">Admin Panel</a></p>
    """)

urlpatterns = [
    path("", include("main.urls")),  # app pages
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('', home_view),
]























