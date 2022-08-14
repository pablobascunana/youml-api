from django.urls import include, path

from .v1 import urls as v1

app_name = 'api'

urlpatterns = [path("v1/", include(v1))]
