from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    game_id = serializers.IntegerField()

    class Meta:
        model = Rating
        fields = (
            'id',
            'game_id',
            'user_id',
            'rating',
        )
        read_only_fields = ('user_id',)

class RatingViewSet(viewsets.ViewSet):
    def create(self, request):
        existing = Rating.objects.filter(
            game_id=request.data['game_id'],
            user=request.auth.user
        ).first()

        if existing:
            existing.rating = request.data['rating']
            existing.save()
            serializer = RatingSerializer(existing)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.auth.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

