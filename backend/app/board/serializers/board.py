from board.models import Board, Column
from board.serializers.ticket import TicketListSerialize
from rest_framework.fields import IntegerField
from rest_framework.serializers import CharField, ModelSerializer, Serializer


class BoardCreateListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name', 'preference', 'owner']
        read_only_fields = ['id']
        extra_kwargs = {'owner': {'write_only': True}}


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

    class Meta:
        model = Column
        fields = ['name', 'board']


class ColumnUpdateSerializer(ModelSerializer):

    class Meta:
        model = Column
        fields = ['name', 'board']
