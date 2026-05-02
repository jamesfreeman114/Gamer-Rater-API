import base64
import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import GamePicture


class GamePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = ('id', 'game_id', 'action_pic')


class GamePictureViewSet(viewsets.ViewSet):

    def create(self, request):
        image_data = request.data.get('image')
        if not image_data or ';base64,' not in image_data:
            return Response({'message': 'A valid image is required'}, status=status.HTTP_400_BAD_REQUEST)
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        decoded_img = base64.b64decode(imgstr)
        file = ContentFile(decoded_img, name=f'{uuid.uuid4()}.{ext}')

        game_picture = GamePicture.objects.create(
            game_id=request.data['game_id'],
            user=request.auth.user,
            action_pic=file
        )
        serializer = GamePictureSerializer(game_picture)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
