from django.urls import path
from .import views
urlpatterns = [
    path('login',views.loginpage,name='login'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    
]
