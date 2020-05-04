from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'add_book$', views.add_book, ),
    url(r'get_geodata', views.get_geodata, ),
]
 