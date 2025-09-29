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
        is_secure = request.is_secure() or request.META.get('HTTP_X_FORWARDED_PROTO') == 'https'
        print(f"DEBUG: Host is '{host}', secure: {is_secure}")
        
        # Define our canonical URL
        canonical_url = f"https://www.plastipallets.com{request.get_full_path()}"
        
        # Check if we need to redirect
        needs_redirect = False
        
        # Case 1: Non-www domain
        if host == 'plastipallets.com':
            needs_redirect = True
            print("DEBUG: Redirect needed - non-www domain")
        
        # Case 2: Not using HTTPS
        elif not is_secure:
            needs_redirect = True
            print("DEBUG: Redirect needed - not HTTPS")
        
        # Perform redirect if needed
        if needs_redirect:
            print(f"DEBUG: Redirecting to: {canonical_url}")
            return HttpResponsePermanentRedirect(canonical_url)
        
        print("DEBUG: No redirect needed")
        return self.get_response(request)