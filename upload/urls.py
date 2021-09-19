from django.urls import path
from django.conf.urls import url
from upload import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^reading$',views.dataupload),
    url(r'readings/([0-9]+)$',views.dataupload),
]