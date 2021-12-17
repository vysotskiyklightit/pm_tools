from board.api import board, ticket
from django.urls import include, path

ticket_comment_urls = [
    path('comments/', ticket.CommentCreateListView.as_view()),
    path('comments/<int:id>/',
         ticket.CommentUpdateRetrieveDeleteView.as_view()),
]

tickets_urls = [
    path('tickets/', ticket.TicketCreateListView.as_view()),
    path('tickets/<int:id>/', ticket.TicketUpdateRetrieveDeleteView.as_view()),
    path('tickets/<int:ticket>/',
         include((ticket_comment_urls, 'tickets_comments'),
                 namespace='tickets_comments')),
]

columns_urls = [
    path('columns/', board.ColumnListCreateView.as_view()),
    path('columns/<int:id>/', board.ColumnUpdateRetrieveDeleteView.as_view()),
    path('columns/<int:column>/',
         include((tickets_urls, 'tickets'), namespace='board_tickets')),
]

urlpatterns = [
    path('boards/', board.BoardCreateListView.as_view()),
    path('boards/<int:id>/', board.BoardUpdateRetrieveView.as_view()),
    path('boards/<int:board>/',
         include((columns_urls, 'columns'), namespace='board_columns')),
]
