from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('Superuser', views.Superuser, name="Superuser"),
    path('additems', views.additems, name="additems"),
    path('deleteitems', views.deleteitems, name="deleteitems"),
    path('logout', views.logout, name="logout"),
    
    path('size/s', views.s, name="s"),
    path('size/m', views.m, name="m"),
    path('size/l', views.l, name="l"),
    path('size/xl', views.xl, name="xl"),
    path('size/xxl', views.xxl, name="xxl"),
    path('size/none', views.none, name="none"),
]
