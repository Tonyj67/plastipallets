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
        
        # Handle ALL redirect cases to https://www.plastipallets.com
        if host == 'plastipallets.com' or not is_secure or host == 'www.plastipallets.com':
            print("DEBUG: Redirect condition met!")
            redirect_url = f"https://www.plastipallets.com{request.get_full_path()}"
            print(f"DEBUG: Redirecting to: {redirect_url}")
            return HttpResponsePermanentRedirect(redirect_url)
        
        print("DEBUG: No redirect needed")
        return self.get_response(request)