from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name="home"),
    #  path("mic/",view,name="mic"),
     path('process/', views.index, name='index'),
]
