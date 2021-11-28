from board.api.bases import PathDependsRelationBoardAPIView
from board.models import Ticket
from board.permissions import IsContributorOrOwnerBoard
from board.serializers.ticket import TicketCreateSerialize, TicketListSerialize
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)


class TicketCreateListView(
    PathDependsRelationBoardAPIView,
    CreateModelMixin,
    ListModelMixin
):
    queryset = Ticket.objects.all()
    permission_classes = [IsContributorOrOwnerBoard]

    def get(self, request, *args, **kwargs):
        self.serializer_class = TicketListSerialize
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = TicketCreateSerialize
        return self.create(request, *args, **kwargs)


class TicketUpdateRetrieveDeleteView(
    PathDependsRelationBoardAPIView,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
):
    queryset = Ticket.objects.all()
    permission_classes = [IsContributorOrOwnerBoard]
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        self.serializer_class = TicketCreateSerialize
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.serializer_class = TicketCreateSerialize
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.serializer_class = TicketCreateSerialize
        return self.delete(request, *args, **kwargs)
