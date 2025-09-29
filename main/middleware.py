# your_project/middleware.py

from django.http import HttpResponsePermanentRedirect

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0].lower()
        
        # If host does NOT start with "www." and ends with your domain, redirect
        if not host.startswith('www.') and host.endswith('plastipallets.com'):
            scheme = 'https' if request.is_secure() or request.META.get('HTTP_X_FORWARDED_PROTO') == 'https' else 'http'
            new_host = 'www.' + host
            redirect_url = f"{scheme}://{new_host}{request.get_full_path()}"
            return HttpResponsePermanentRedirect(redirect_url)
        
        return self.get_response(request)






















