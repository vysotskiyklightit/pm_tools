from board.models import Ticket, TicketComment
from board.serializers.fields import (ColumnPathParamsDefault,
                                      TicketPathParamsDefault,
                                      TokenUserDefault)
from rest_framework.fields import CharField, HiddenField, IntegerField
from rest_framework.serializers import (ModelSerializer,
                                        PrimaryKeyRelatedField, Serializer)
from user.serializers.user import UserCommentSerializer


class TicketListSerialize(Serializer):
    id = IntegerField()
    name = CharField()
    executor = PrimaryKeyRelatedField(read_only=True)


class TicketRetrieveSerialize(TicketListSerialize):
    description = CharField()


class TicketCreateSerialize(ModelSerializer):
    column_id = HiddenField(default=ColumnPathParamsDefault())

    class Meta:
        model = Ticket
        fields = ['name', 'executor', 'column_id', 'description']
        read_only_fields = ['id']


class TicketUpdateSerialize(TicketCreateSerialize):
    class Meta:
        model = Ticket
        fields = ['name', 'executor', 'column_id']


class TicketCommentListRetrieveSerialize(Serializer):
    id = IntegerField()
    owner = UserCommentSerializer()
    head_comment = PrimaryKeyRelatedField(read_only=True)
    message = CharField()


class TicketCommentCreateSerialize(ModelSerializer):
    owner = HiddenField(default=TokenUserDefault())
    ticket_id = HiddenField(default=TicketPathParamsDefault())

    class Meta:
        model = TicketComment
        fields = ['id', 'ticket_id', 'owner', 'head_comment', 'message']
        read_only_fields = ['id']


class TicketCommentUpdateSerialize(ModelSerializer):
    ticket_id = HiddenField(default=TicketPathParamsDefault())

    class Meta:
        model = TicketComment
        fields = ['id', 'ticket_id', 'message']
        read_only_fields = ['id']
