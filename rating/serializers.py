from rest_framework import serializers
from .models import Comic, Rating

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ['id', 'title', 'author', 'rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'comic', 'user', 'value']