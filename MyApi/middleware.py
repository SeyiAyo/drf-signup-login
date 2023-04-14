from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class CorsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE'
        response['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type, Authorization'
        return response

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE'
        response['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type, Authorization'
        return response
