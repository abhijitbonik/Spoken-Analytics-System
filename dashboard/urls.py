from django.urls import path
from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url('', views.index),
]