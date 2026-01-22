from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse


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
            return JsonResponse({"error":"only api access allowed"},status=404)
        
        response=self.get_response(request)

        #after getting response from view

        print("after view Middleware hit:")

        return response

blocled_list = ['172.16.22.11']


class BlockIPMiddleware:
    
    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")

        return ip
    

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):

        ip = BlockIPMiddleware.get_client_ip(request)

        if ip in blocled_list:
            return JsonResponse({"error":"You are not allowed to access this site"},status=401)

        
        return self.get_response(request)