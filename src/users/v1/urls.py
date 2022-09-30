from rest_framework import routers

from users.viewsets.user.view import UserViewSet

router = routers.SimpleRouter()

urlpatterns = []

router.register("user", UserViewSet)

urlpatterns += router.urls
