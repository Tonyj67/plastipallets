# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def products(request):
    return render(request, "products.html")

def contact(request):
    return render(request, "contact.html")
    return render(request, "all_products.html")

def flat_top_hd(request):
    return render(request, "flat_top_hd.html")

def heavy_duty_grid(request):
    return render(request, "heavy_duty_grid.html")

def light_flat(request):
    return render(request, "light_flat.html")

def light_grid(request):
    return render(request, "light_grid.html")

def nestable(request):
    return render(request, "nestable.html")

def all_products(request):
    return render(request, "products.html")

















































