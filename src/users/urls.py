from django.urls import include, path

from .v1 import urls as v1

app_name = 'users'

urlpatterns = [path("v1/", include(v1))]
