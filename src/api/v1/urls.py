from rest_framework import routers

from src.api.viewsets.user import UserViewSet

router = routers.SimpleRouter()

urlpatterns = []

router.register("users", UserViewSet)

urlpatterns += router.urls
