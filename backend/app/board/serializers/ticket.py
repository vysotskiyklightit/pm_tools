from board.models import Ticket, TicketComment
from board.serializers.utils import TokenUserDefault
from django.contrib.auth.models import User
from rest_framework.fields import (CharField, CurrentUserDefault, HiddenField,
                                   IntegerField)
from rest_framework.serializers import (ModelSerializer,
                                        PrimaryKeyRelatedField, Serializer)
from user.serializers.user import UserCommentSerializer


class TicketListSerialize(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'name', 'executor']


class TicketRetrieveSerialize(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketCreateSerialize(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketUpdateSerialize(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['name', 'executor', 'column']


class TicketCommentListRetrieveSerialize(Serializer):
    id = IntegerField()
    owner = UserCommentSerializer()
    head_comment = PrimaryKeyRelatedField(read_only=True)
    message = CharField()


class TicketCommentCreateSerialize(ModelSerializer):
    owner = HiddenField(default=TokenUserDefault())

    class Meta:
        model = TicketComment
        fields = ['id', 'ticket', 'owner', 'head_comment', 'message']
        read_only_fields = ['id']


class TicketCommentUpdateSerialize(ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'
