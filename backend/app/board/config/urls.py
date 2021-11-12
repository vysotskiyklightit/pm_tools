from board.api import board
from django.urls import path

urlpatterns = [
    path('board/', board.BoardCreateListView.as_view()),
    path('board/<id>/', board.BoardUpdateRetrieveView.as_view()),
    path('board/<board_id>/columns/', board.ColumnListCreateView.as_view())
]
