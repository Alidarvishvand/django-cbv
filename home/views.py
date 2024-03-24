from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from . models import Car
from django.views.generic import TemplateView,RedirectView,MonthArchiveView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView,CreateView,DeleteView,UpdateView
from .form import CarCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
from django.contrib.auth import views as auth_views


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
    
class home2(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
    
        context['cars'] = Car.objects.all()
        return context
    
class tow(RedirectView):
    pattern_name = 'home:home'
    query_string= False

    def get_redirect_url(self, *args, **kwargs):
        print('='*90)
        print('processing your request...')
        print(kwargs['name'],print(kwargs['id']))
        kwargs.pop('name')
        kwargs.pop('id')
        return super().get_redirect_url(*args, **kwargs)
    

class cardetail(DetailView):
    template_name = 'detail.html'
    model = Car
    def __str__(self):
        return self.model
    


# class CreatCarView(FormView):
#     template_name = 'home/create.html'
#     form_class = CarCreateForm
#     success_url = reverse_lazy('home:home')

#     def form_valid(self, form):
#         self._create_car(form.cleaned_data)
#         messages.success(self.request,'create car successfully','success')
#         return super().form_valid(form)
#     def _create_car(self,data):
#         Car.objects.create(name=data['name'],owner=data['owner'],year=data['year'])


class CreateCarView(CreateView):
    model = Car
    fields = ['name','year']
    template_name = 'home/create.html'

    success_url = reverse_lazy('home:home')

    def form_valid(self,form):
        car = form.save(commit=False)
        car.owner = self.request.user.username
        car.save()
        messages.success(self.request,'create car successfully','success')
        return super().form_valid(form)
    

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('home:home')
    template_name = 'home/delete.html'


class Carupdate(UpdateView):
    model = Car
    fields = ['name']
    success_url = reverse_lazy('home:home')
    template_name = 'home/update.html'


class UserLogin(auth_views.LoginView):
    template_name = 'home/login.html'
    next_page = reverse_lazy('home:home')

class UserLogout(auth_views.LogoutView):
    next_page = reverse_lazy('home:home')


class MonthCar(MonthArchiveView):
    model = Car
    date_field = 'created'
    template_name = 'home/home.html'
    context_object_name = 'cars'
    month_format='%m'