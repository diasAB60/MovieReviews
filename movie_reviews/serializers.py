from rest_framework import serializers
from.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'rating', 'description']

    def validate_rating(self, value):
        if value > 10 or value < 1:
            raise serializers.ValidationError('Rating must be between 1 and 10')