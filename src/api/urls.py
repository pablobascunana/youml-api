from django.urls import path
from rest_framework.routers import SimpleRouter

from .viewsets.company.view import CompanyViewSet
from .viewsets.dataset.view import DatasetViewSet
from .viewsets.project.view import ProjectViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = []

router.register("company", CompanyViewSet)
router.register("project", ProjectViewSet)
router.register("dataset", DatasetViewSet)

urlpatterns += router.urls
