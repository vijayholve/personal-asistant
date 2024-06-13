from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name="home"),
    #  path("mic/",view,name="mic"),
     path('', views.index, name='index'),
]
