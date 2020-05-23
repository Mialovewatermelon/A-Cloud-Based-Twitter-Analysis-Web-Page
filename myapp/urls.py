from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    url(r'get_geodata', views.get_geodata, ),
    url(r'get_data', views.get_data),
    url(r'information/get_info', views.get_information_data),
    url(r'information/send_info', views.send_information_data),
    url(r'^$', views.index)
]
 