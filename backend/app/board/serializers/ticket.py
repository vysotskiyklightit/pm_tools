from board.models import Ticket, TicketComment
from rest_framework.fields import CharField, IntegerField
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
    class Meta:
        model = TicketComment
        fields = '__all__'


class TicketCommentUpdateSerialize(ModelSerializer):
    class Meta:
        model = TicketComment
        fields = ['message']
