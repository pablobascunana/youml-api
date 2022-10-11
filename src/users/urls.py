from rest_framework.routers import SimpleRouter

from .viewsets.auth.view import AuthViewSet
from .viewsets.user.view import UserViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = []

router.register("user", UserViewSet)
router.register("auth", AuthViewSet)

urlpatterns += router.urls
