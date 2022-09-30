from django.urls import include, path

urlpatterns = [
    path('users/v1/', include("users.urls"))
]
