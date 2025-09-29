# your_project/middleware.py
# your_project/middleware.py
print("DEBUG: Middleware module is being loaded!")  # This shows on server start
from django.http import HttpResponsePermanentRedirect

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Use HTTP_HOST directly — more reliable in Heroku/CDN setups
        host = request.META.get('HTTP_HOST', '').split(':')[0].lower()

        # If host is non-www, redirect to www
        if host == 'plastipallets.com':
            scheme = 'https' if request.is_secure() or request.META.get('HTTP_X_FORWARDED_PROTO') == 'https' else 'http'
            redirect_url = f"{scheme}://www.plastipallets.com{request.get_full_path()}"
            return HttpResponsePermanentRedirect(redirect_url)

        return self.get_response(request)

















