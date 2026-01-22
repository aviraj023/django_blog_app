from rest_framework.response import Response
from django.http import HttpResponse


class SimpleMiddleware:
    def __init__(self,get_response):

        print("****Middleware initialized")

        self.get_response=get_response

    
    def __call__(self,request):

        #before hitting view
        print("****before view Middleware hit:")


        if not request.path.startswith('/blog/'):
            return HttpResponse({"error":"only api access allowed"},status=404)
        
        response=self.get_response(request)

        #after getting response from view

        print("after view Middleware hit:")

        return response



