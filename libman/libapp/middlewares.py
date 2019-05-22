from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("In process request")
        request.META['var'] = "hello"

    def process_response(self, request, response):
        print("In process response")
        response = request.META.get('var')
        return response

