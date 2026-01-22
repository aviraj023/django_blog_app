from rest_framework.response import Response
from django.http import HttpResponse


class SimpleMiddleware:
    def __init__(self,get_response):

        print("****Middleware initialized")

        self.get_response=get_response

    
    def __call__(self,request):

        #before hitting view
        print("****before view Middleware hit:")

        # to allow to hit admin
        if request.path.startswith('/admin/') or request.path.startswith('/static'):
            return self.get_response(request)

        if not request.path.startswith('/blog/'):
            return HttpResponse({"error":"only api access allowed"},status=404)
        
        response=self.get_response(request)

        #after getting response from view

        print("after view Middleware hit:")

        return response



