from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    url(r'add_book$', views.add_book, ),
    url(r'get_geodata', views.get_geodata, ),
    url(r'get_data', views.get_data),
    url(r'^$', views.index)
]
 