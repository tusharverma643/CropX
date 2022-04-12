from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('profile/',views.userprofile,name='userprofile'),
    path('',views.home,name="home")
] 


