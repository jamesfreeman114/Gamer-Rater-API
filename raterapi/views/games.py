from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import Game, GamePicture
from raterapi.views.reviews import ReviewSerializer
from django.db.models import Q


class GamePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = ('id', 'action_pic')



class GameSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    pictures = GamePictureSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)
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
            'reviews',
            'pictures',
            'average_rating'
        )


class GameViewSet(viewsets.ViewSet):

    def list(self, request):
        
        search_text = self.request.query_params.get('q', None)

        if search_text:
            games = Game.objects.filter(
                Q(title__contains=search_text) |
                Q(description__contains=search_text) |
                Q(designer__contains=search_text)
            )
        else:
            games = Game.objects.all()

        orderby = self.request.query_params.get('orderby', None)
        if orderby:
            games = games.order_by(orderby)
            
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response({'message': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.auth.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            return Response({'message': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)

        if game.user != request.auth.user:
            return Response({'message': 'You do not have permission to edit this game'}, status=status.HTTP_403_FORBIDDEN)

        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
