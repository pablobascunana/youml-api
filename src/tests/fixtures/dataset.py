import pytest
from model_bakery import baker

from api.viewsets import Project, Label, Image, ImageLabels
from api.viewsets.dataset.model import Dataset


@pytest.fixture()
def dataset() -> Dataset:
    return baker.make(Dataset)


@pytest.fixture()
def dataset_to_train(project: Project) -> Dataset:
    dataset = baker.make(Dataset, project=project)
    label = baker.make(Label)
    image = baker.make(Image)
    baker.make(ImageLabels, image=image, label=label)
    return dataset
