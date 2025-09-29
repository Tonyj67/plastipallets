# your_project/middleware.py
from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0].lower()
        print(f"DEBUG: Host is '{host}'")  # This will show in logs
        
        # If host does NOT start with "www." and ends with your domain, redirect
        if not host.startswith('www.') and host.endswith('plastipallets.com'):
            print("DEBUG: Redirecting non-www to www")
            # Always redirect to HTTPS www
            redirect_url = f"https://www.plastipallets.com{request.get_full_path()}"
            print(f"DEBUG: Redirecting to: {redirect_url}")
            return HttpResponsePermanentRedirect(redirect_url)
        
        print("DEBUG: No redirect needed")
        return self.get_response(request)



































