from board.models import Board
from django.contrib import admin


@admin.register(Board)
class AdminBoard(admin.ModelAdmin):
    pass
