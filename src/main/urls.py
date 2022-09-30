from django.urls import include, path

api_version = '/v1/'


urlpatterns = [
    path(f"users{api_version}", include("users.urls")),
    path(f"api{api_version}", include("api.urls"))
]
