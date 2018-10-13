from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    path('mobile_api/client/create', views.client_create),
    path('mobile_api/urns/list', views.get_urns_workload),
    path('mobile_api/open_bin', views.get_urns_workload)
]