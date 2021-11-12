from enum import Enum


class EnumChoicesBase(Enum):

    @classmethod
    def choices(cls):
        return tuple((field.name, field.value) for field in cls)


class BoardPreference(EnumChoicesBase):
    public = 'public'
    private = 'private'
