from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^[a-zA-Z0-9]{5}$', views.link, name='link'),
    
]
