from django.contrib.auth.models import User


class TokenUserDefault(object):
    requires_context = True

    def __call__(self, serializer_field):
        return User.objects.get(id=serializer_field.context['request'].user.id)
