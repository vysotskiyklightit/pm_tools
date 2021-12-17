from abc import ABC, abstractmethod


class IService(ABC):

    @abstractmethod
    def execute(self):
        pass


class IPresenter(ABC):

    @abstractmethod
    def present(self):
        pass


class IPreprocessors(ABC):

    @abstractmethod
    def process(self):
        pass
