from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup/', views.sign_up, name='sign_up'),

]