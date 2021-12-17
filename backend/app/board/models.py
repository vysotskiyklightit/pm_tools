from common.constants import BoardPreference
from django.db import models


class Board(models.Model):
    owner = models.ForeignKey(
        'user_auth.User',
        on_delete=models.CASCADE
    )
    contributors = models.ManyToManyField(
        'user_auth.User',
        related_name='contributors'
    )
    name = models.CharField(max_length=120)
    preference = models.CharField(
        max_length=50,
        choices=BoardPreference.choices(),
        null=False
    )


class Column(models.Model):
    board = models.ForeignKey('board.Board', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)


class Ticket(models.Model):
    column = models.ForeignKey(
        'board.Column',
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    name = models.CharField(max_length=120)
    executor = models.ForeignKey(
        'user_auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField()


class TicketComment(models.Model):
    ticket = models.ForeignKey(
        'board.Ticket',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    owner = models.ForeignKey(
        'user_auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    head_comment = models.ForeignKey(
        'board.TicketComment',
        on_delete=models.SET_NULL,
        related_name='head_comments',
        default=None,
        null=True,
        blank=True,
    )
    message = models.TextField(max_length=500)
