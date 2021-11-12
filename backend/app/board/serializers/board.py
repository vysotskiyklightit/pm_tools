from board.models import Board, Column
from board.serializers.ticket import TicketListSerialize
from rest_framework.serializers import CharField, ModelSerializer, Serializer


class BoardCreateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'preference']


class BoardUpdateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'preference', 'contributors']


class BoardRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class BoardListSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'preference']


class ColumnListSerializer(Serializer):
    name = CharField()
    tickets = TicketListSerialize(many=True)


class ColumnCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Column
        fields = '__all__'
