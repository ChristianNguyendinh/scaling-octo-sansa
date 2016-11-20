from rest_framework import serializers
from .models import Artist, Article

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist;

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article;