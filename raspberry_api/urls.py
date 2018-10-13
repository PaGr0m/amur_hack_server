from django.urls import path
from . import views


urlpatterns = [
    path('raspberry_api/urn', views.update_urn),
]