# main/views.py
from django.shortcuts import render
import ssl
from django.core.mail import send_mail
from django.shortcuts import render, redirect

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

def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send email
        send_mail(
            subject=f"New Inquiry from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
            from_email='joubert.tony@gmail.com',
            recipient_list=['joubert.tony@gmail.com'],
            fail_silently=False,
        )

        return redirect('thank_you')

    return render(request, 'contact.html')















































