from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.


class home(View):
    http_method_names = ['post','options']


    def get(self, request):
        return render(request, 'home/home.html')
    
    def options(self, request,*args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers['host'] = 'localhost'
        response.headers['user'] = request.user
        return response
    
    def http_method_not_allowed(self, request: HttpRequest, *args, **kwargs):
        super().http_method_not_allowed(request, *args, **kwargs)
        return render (request, 'method_not_allowed.html')  