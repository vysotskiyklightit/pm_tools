from django.contrib.auth.models import User


class TokenUserDefault(object):
    requires_context = True

    def __call__(self, serializer_field) -> User:
        return User.objects.get(id=serializer_field.context['request'].user.id)


class PathParamsDefault(object):
    requires_context: bool = True
    FIELD_NAME: str = None

    def __call__(self, serializer_field):
        kwargs = serializer_field.context['view'].kwargs
        return int(kwargs[self.FIELD_NAME])


class BoardPathParamsDefault(PathParamsDefault):
    FIELD_NAME: str = 'board'


class ColumnPathParamsDefault(PathParamsDefault):
    FIELD_NAME: str = 'column'


class TicketPathParamsDefault(PathParamsDefault):
    FIELD_NAME: str = 'ticket'
