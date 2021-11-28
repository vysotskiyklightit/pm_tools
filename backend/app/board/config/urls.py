from board.api import board, ticket
from django.urls import include, path

ticket_comment_urls = [
    path('comment/', ticket.CommentCreateListView.as_view()),
    path('comment/<id>/', ticket.CommentUpdateRetrieveDeleteView.as_view()),
]

tickets_urls = [
    path('ticket/', ticket.TicketCreateListView.as_view()),
    path('ticket/<id>/', ticket.TicketUpdateRetrieveDeleteView.as_view()),
    path('ticket/<ticket>/',
         include((ticket_comment_urls, 'tickets_comments'),
                 namespace='tickets_comments')),
]

columns_urls = [
    path('column/', board.ColumnListCreateView.as_view()),
    path('column/<id>/', board.ColumnUpdateRetrieveDeleteView.as_view()),
    path('column/<column>/',
         include((tickets_urls, 'tickets'), namespace='board_tickets')),
]

urlpatterns = [
    path('board/', board.BoardCreateListView.as_view()),
    path('board/<id>/', board.BoardUpdateRetrieveView.as_view()),
    path('board/<board>/',
         include((columns_urls, 'columns'), namespace='board_columns')),
]
