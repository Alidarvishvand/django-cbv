from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('cars/',views.home2.as_view(),name='home'),
    path('tow/<int:id>/<str:name>/',views.tow.as_view(),name='tow'),
    path('car/<int:pk>/',views.cardetail.as_view(),name='cardetail'),
    path('create/', views.CreateCarView.as_view(),name='create'),
]
