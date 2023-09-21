from rest_framework import serializers
from classifiers.models import Movie, Sentiment

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title'
        )

class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment
        fields = (
            'id',
            'movie_title',
            'reviews',
            'results',
            'gender',
            'age',
            'country',
            'timestamp'
        )
