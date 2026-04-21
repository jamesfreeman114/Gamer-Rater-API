from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'description',
            'designer',
            'year_released',
            'num_players',
            'estimated_time',
            'age_recommendation',
            'user_id',
        )


class GameViewSet(viewsets.ViewSet):

    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.auth.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
