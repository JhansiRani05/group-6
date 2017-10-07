from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^$', views.index ,name = "index") ,
    url(r'^get/$', views.getdata ,name ="get"),
    url(r'^temp',views.temp,name='temp'),
    url(r'^index',views.index,name="index"),
    url(r'^micro',views.micro,name="micro"),
   
]
