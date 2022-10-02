from rest_framework.routers import SimpleRouter

from .viewsets.company.view import CompanyViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = []

router.register("company", CompanyViewSet)

urlpatterns += router.urls
