# main/views.py
from django.shortcuts import render
import ssl
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime



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
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # --- 1. Email to you (site owner)
        send_mail(
            subject=f"New Inquiry from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # --- 2. Professional reply to visitor
        context = {
            "name": name or "Friend",
            'user_email': email,
            "year": datetime.now().year,
            'support_email': 'joubert.tony@gmail.com.com',
        }

        # Send thank you email to visitor
        html_content = render_to_string("emails/thank_you_email.html", context)
        text_content = strip_tags(html_content)

        email_msg = EmailMultiAlternatives(
            subject="Thank you for contacting Plasti Pallets",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        email_msg.attach_alternative(html_content, "text/html")
        email_msg.send()

        # Render thank you page
        return render(request, 'emails/thank_you_email.html', context)

    return JsonResponse({"status": "error"}, status=400)










































































