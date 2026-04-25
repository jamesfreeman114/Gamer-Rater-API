from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from raterapi.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'game_id',
            'user_id',
            'content',
        )
        read_only_fields = ('user_id',)

class ReviewViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.auth.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)