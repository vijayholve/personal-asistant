from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    #  path("mic/",view,name="mic"),
    path("index/",views.index,name="mic2"),
path('process/', views.process_speech, name='process_speech'),
]
