from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Comic, Rating
from .serializers import ComicSerializer, RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comic_id = serializer.validated_data['comic']
        user_id = serializer.validated_data['user']

        rating, _ = Rating.objects.update_or_create(
            comic=comic_id, user=user_id,
            defaults={'value': serializer.validated_data['value']}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def comic_rating(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    serializer = ComicSerializer(comic)
    return Response(serializer.data)