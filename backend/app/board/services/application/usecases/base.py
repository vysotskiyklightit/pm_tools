from abc import ABC, abstractmethod

from rest_framework.request import Request


class BaseApplicationRequestCase(ABC):

    def __init__(self, request: Request, *args, **kwargs):
        self._request = request
        self._args = args
        self._kwargs = kwargs


class BaseCreateCase(BaseApplicationRequestCase):

    @abstractmethod
    def create(self):
        pass


class BaseListCase(BaseApplicationRequestCase):

    @abstractmethod
    def list(self):
        pass
