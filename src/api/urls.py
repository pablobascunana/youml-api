from rest_framework.routers import SimpleRouter

from .viewsets.company.view import CompanyViewSet
from .viewsets.project.view import ProjectViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = []

router.register("company", CompanyViewSet)
router.register("project", ProjectViewSet)

urlpatterns += router.urls
