from rest_framework import routers

from api.viewsets.hello_world import HelloWorldViewSet

router = routers.SimpleRouter()

urlpatterns = []

router.register("hello", HelloWorldViewSet)

urlpatterns += router.urls
