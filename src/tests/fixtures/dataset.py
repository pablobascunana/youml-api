from typing import Tuple

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from api.viewsets import Project, Label, Image, ImageLabels, Training
from api.viewsets.dataset.model import Dataset
from core.utils.date import date_now


@pytest.fixture()
def dataset() -> Dataset:
    return baker.make(Dataset)


@pytest.fixture()
def dataset_to_train(project: Project) -> Dataset:
    dataset = baker.make(Dataset, project=project)
    label = baker.make(Label)
    image = baker.make(Image)
    baker.make(ImageLabels, image=image, label=label)
    baker.make(Training)
    return dataset


@pytest.fixture()
def dataset_to_train_with_admin_user(client_as_admin: APIClient, project: Project) -> Tuple[APIClient, Dataset]:
    dataset = baker.make(Dataset, project=project, user=client_as_admin[1])
    image = baker.make(Image, mark_to_train_at=date_now())
    label = baker.make(Label, dataset=dataset)
    baker.make(ImageLabels, image=image, label=label, mark_to_train_at=date_now())
    baker.make(Training, dataset=dataset, user=client_as_admin[1])
    return client_as_admin, dataset


@pytest.fixture()
def dataset_to_train_with_normal_user(client_as_user: APIClient, project: Project) -> Tuple[APIClient, Dataset]:
    dataset = baker.make(Dataset, project=project, user=client_as_user[1])
    image = baker.make(Image, mark_to_train_at=date_now())
    label = baker.make(Label, dataset=dataset)
    baker.make(ImageLabels, image=image, label=label, mark_to_train_at=date_now())
    baker.make(Training, dataset=dataset, user=client_as_user[1])
    return client_as_user, dataset
