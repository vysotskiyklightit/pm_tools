from board.models import Ticket
from rest_framework.serializers import ModelSerializer


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
