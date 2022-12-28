from rest_framework.routers import SimpleRouter

from .viewsets.company.view import CompanyViewSet
from .viewsets.dataset.view import DatasetViewSet
from .viewsets.image.view import ImageViewSet
from .viewsets.image_labels.view import ImageLabelViewSet
from .viewsets.label.view import LabelViewSet
from .viewsets.project.view import ProjectViewSet
from .viewsets.training.view import TrainingViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = []

router.register("company", CompanyViewSet)
router.register("project", ProjectViewSet)
router.register("dataset", DatasetViewSet)
router.register("label", LabelViewSet)
router.register("image", ImageViewSet)
router.register("image-label", ImageLabelViewSet)
router.register("train", TrainingViewSet)

urlpatterns += router.urls
