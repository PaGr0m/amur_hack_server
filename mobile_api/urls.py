from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    # path('beacons', views.beacons_index),
    path('mobile_api/client/create', views.client_create),
    path('mobile_api/open_bin', views.open_bin)
]