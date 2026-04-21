from django.db import models
from django.conf import settings


class Rating(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_ratings'
    )
    rating = models.IntegerField()

    class Meta:
        unique_together = ('game', 'user')


