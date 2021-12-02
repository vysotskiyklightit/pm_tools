from board.api.bases import PathDependsRelationBoardAPIView
from board.config.utils import method_permission
from board.models import Ticket, TicketComment
from board.permissions import IsContributorOrOwnerBoardFromPath
from board.serializers.ticket import (TicketCommentCreateSerialize,
                                      TicketCommentListRetrieveSerialize,
                                      TicketCommentUpdateSerialize,
                                      TicketCreateSerialize,
                                      TicketListSerialize,
                                      TicketRetrieveSerialize,
                                      TicketUpdateSerialize)
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)


class TicketCreateListView(
    PathDependsRelationBoardAPIView,
    CreateModelMixin,
    ListModelMixin
):
    """
    View for create or present list of tickets
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerialize
    permission_classes = [IsContributorOrOwnerBoardFromPath]

    @swagger_auto_schema(tags=['ticket'])
    def get(self, request, *args, **kwargs):
        self.serializer_class = TicketListSerialize
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['ticket'])
    def post(self, request, *args, **kwargs):
        self.serializer_class = TicketCreateSerialize
        return self.create(request, *args, **kwargs)


class TicketUpdateRetrieveDeleteView(
    PathDependsRelationBoardAPIView,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
):
    """
    View for update delete, or present tickets
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketRetrieveSerialize
    permission_classes = [IsContributorOrOwnerBoardFromPath]
    lookup_field = 'id'

    @swagger_auto_schema(tags=['ticket'])
    def get(self, request, *args, **kwargs):
        self.serializer_class = TicketRetrieveSerialize
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['ticket'])
    def put(self, request, *args, **kwargs):
        self.serializer_class = TicketUpdateSerialize
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['ticket'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentCreateListView(
    PathDependsRelationBoardAPIView,
    CreateModelMixin,
    ListModelMixin
):
    """
    View for create or present list of tickets
    """
    queryset = TicketComment.objects.all()
    serializer_class = TicketCommentCreateSerialize
    permission_classes = [IsContributorOrOwnerBoardFromPath]

    @swagger_auto_schema(tags=['comment'])
    def get(self, request, *args, **kwargs):
        self.serializer_class = TicketCommentListRetrieveSerialize
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['comment'])
    def post(self, request, *args, **kwargs):
        self.serializer_class = TicketCommentCreateSerialize
        return self.create(request, *args, **kwargs)


class CommentUpdateRetrieveDeleteView(
    PathDependsRelationBoardAPIView,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin
):
    """
    View for update delete, or present tickets
    """
    queryset = TicketComment.objects.all()
    permission_classes = [IsContributorOrOwnerBoardFromPath]
    serializer_class = TicketCommentListRetrieveSerialize
    lookup_field = 'id'

    @swagger_auto_schema(tags=['comment'])
    def get(self, request, *args, **kwargs):
        self.serializer_class = TicketCommentListRetrieveSerialize
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['comment'])
    @method_permission([IsContributorOrOwnerBoardFromPath])
    def put(self, request, *args, **kwargs):
        self.serializer_class = TicketCommentUpdateSerialize
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['comment'])
    @method_permission([IsContributorOrOwnerBoardFromPath])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
