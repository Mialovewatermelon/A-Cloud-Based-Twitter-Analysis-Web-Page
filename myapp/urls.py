from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    url(r'get_geodata', views.get_geodata, ),
    url(r'^$', views.index)
]
 