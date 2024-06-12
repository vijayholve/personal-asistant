from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
     path("mic/",views.mic,name="mic"),
          path("mic/",views.mic,name="mic"),

]
