from typing import Generic, TypeVar

from django.db.models import Model


class BaseEntity:
    pass


ModelType = TypeVar('ModelType', bound=Model)
EntityType = TypeVar('EntityType', bound=BaseEntity)


class BaseDAO(Generic[ModelType, EntityType]):

    def __init__(self, model):
        self._model = model

    def _to_entity(self, instance) -> EntityType:
        raise NotImplementedError
