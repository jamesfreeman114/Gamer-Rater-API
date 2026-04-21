from django.db import models
from django.conf import settings

class GamePicture(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        related_name='pictures'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_pictures'

    )
    image = models.CharField(max_length=200)