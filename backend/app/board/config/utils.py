from abc import ABC, abstractmethod


class IService(ABC):

    @abstractmethod
    def execute(self):
        pass


class IPresenter(ABC):

    @abstractmethod
    def present(self):
        pass


def method_permission(permissions):
    def wrapper(func):
        def method(self, request, *args, **kwargs):
            self.permission_classes = permissions
            self.check_permissions(request)
            return func(self, request, *args, **kwargs)

        return method

    return wrapper
