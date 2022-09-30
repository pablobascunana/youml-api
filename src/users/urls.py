from rest_framework.routers import SimpleRouter

from .viewsets.user.view import UserViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = []

router.register("user", UserViewSet)

urlpatterns += router.urls
