from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('cars/',views.home2.as_view(),name='home'),
    path('tow/<int:id>/<str:name>/',views.tow.as_view(),name='tow'),
    path('car/<int:pk>/',views.cardetail.as_view(),name='cardetail'),
    path('create/', views.CreateCarView.as_view(),name='create'),
    path('delete/<int:pk>/', views.CarDelete.as_view(),name= 'car_delete'),
    path('update/<int:pk>/', views.Carupdate.as_view(),name= 'car_update'),
    path('login/',views.UserLogin.as_view(),name='user_login'),
    path('logout/',views.UserLogout.as_view(),name='user_logout'),
    path ('<int:year>/<int:month>/', views.MonthCar.as_view()),

]