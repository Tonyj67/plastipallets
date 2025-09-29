# your_project/middleware.py
# your_project/middleware.py
print("DEBUG: Middleware module is being loaded!")

from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        print("DEBUG: Middleware instance created!")
        self.get_response = get_response

    def __call__(self, request):
        host = request.META.get('HTTP_HOST', '').split(':')[0].lower()
        
        # Cloudflare headers for SSL detection
        cf_visitor = request.META.get('HTTP_CF_VISITOR', '')
        x_forwarded_proto = request.META.get('HTTP_X_FORWARDED_PROTO', '')
        x_forwarded_proto_heroku = request.META.get('HTTP_X_FORWARDED_PROTO', '')
        
        # Determine if request is secure (handles Cloudflare)
        is_secure = (
            request.is_secure() or 
            x_forwarded_proto == 'https' or 
            x_forwarded_proto_heroku == 'https' or
            '"scheme":"https"' in cf_visitor
        )
        
        print(f"DEBUG: Host: '{host}', Secure: {is_secure}")
        print(f"DEBUG: CF_VISITOR: {cf_visitor}")
        print(f"DEBUG: X_FORWARDED_PROTO: {x_forwarded_proto}")
        
        # Redirect conditions
        if host == 'plastipallets.com' or (host == 'www.plastipallets.com' and not is_secure):
            redirect_url = f"https://www.plastipallets.com{request.get_full_path()}"
            print(f"DEBUG: Redirecting to: {redirect_url}")
            return HttpResponsePermanentRedirect(redirect_url)
        
        print("DEBUG: No redirect needed")
        return self.get_response(request)