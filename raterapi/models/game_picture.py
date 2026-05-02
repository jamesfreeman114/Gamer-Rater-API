from django.db import models
from django.conf import settings

class GamePicture(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.DO_NOTHING,
        related_name='pictures'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_pictures'

    )
    action_pic = models.ImageField(
        upload_to='actionimages', height_field=None,
        width_field=None, max_length=None, null=True)