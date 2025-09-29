from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Remove port if present
        
        # Redirect plastipallets.com → www.plastipallets.com
        if host == 'plastipallets.com':
            print("DEBUG: Redirecting to www version")  # Debug line
            return HttpResponsePermanentRedirect(
                'https://www.plastipallets.com' + request.get_full_path()
            )
        
        return self.get_response(request)
        return response