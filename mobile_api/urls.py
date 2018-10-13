from django.urls import path
from . import views


urlpatterns = [
    path('mobile_api/client/authorization', views.authorization),
    path('mobile_api/client/create', views.client_create),
    path('mobile_api/urns/list', views.get_urns_workload)
]