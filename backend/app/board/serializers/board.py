from board.models import Board, Column
from board.serializers.fields import BoardPathParamsDefault, TokenUserDefault
from board.serializers.ticket import TicketListSerialize
from rest_framework.fields import HiddenField, IntegerField
from rest_framework.serializers import CharField, ModelSerializer, Serializer


class BoardCreateSerializer(ModelSerializer):
    owner = HiddenField(default=TokenUserDefault())

    class Meta:
        model = Board
        fields = ['name', 'preference', 'owner']


class BoardListSerializer(Serializer):
    id = IntegerField()
    name = CharField()
    preference = CharField()


class BoardRetrieveUpdateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ['id', 'owner']


class ColumnListRetrieveSerializer(Serializer):
    id = IntegerField()
    name = CharField()
    tickets = TicketListSerialize(many=True)


class ColumnCreateSerializer(ModelSerializer):
    board_id = HiddenField(default=BoardPathParamsDefault())

    class Meta:
        model = Column
        fields = ['id', 'name', 'board_id']
        read_only_fields = ['id']


class ColumnUpdateSerializer(ColumnCreateSerializer):

    class Meta:
        model = Column
        fields = ['id', 'name']
        read_only_fields = ['id']
