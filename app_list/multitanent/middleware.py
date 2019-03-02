from django.utils.deprecation import MiddlewareMixin
import pprint

class TanentDetectionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def process_request(self, request):
        pprint.pprint(request.META)
        return None