from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Artist, Article
from rest_framework import generics
from .serializers import ArtistSerializer, ArticleSerializer
from .queries import get_news_articles


class InfoTestView(TemplateView):
	template_name = 'info.html'
	def get_context_data(self, **kwargs):
		context = super(InfoTestView, self).get_context_data(**kwargs)
		context['searchName'] = self.kwargs['name']
		return context

class SearchView(TemplateView):
	template_name = 'search.html'

#class SubArtistDetail(generics.RetrieveAPIView):
#	lookup_field = 'subName'
#	queryset = Artist.objects.all()
#	serializer_class = ArtistSerializer

class SubArtistDetail(generics.RetrieveAPIView):
	lookup_field = 'subName'
	serializer_class = ArtistSerializer
	def get_queryset(self):
		sName = self.kwargs['subName']
		artist = Artist.objects.filter(subName=sName)
		if (len(artist) == 0):
			print("warning ------ THIS IS WHERE CALL TO POPULATE GOES! ------- warning")
			newName = self.kwargs['subName'].replace("-", " ")
			a = Artist(name=newName)
			a.save()
			artist = Artist.objects.filter(subName=a.subName)
		print("DONE POPULATING ARTIST")
		return artist

class ArticleDetail(generics.ListAPIView):
	serializer_class = ArticleSerializer
	def get_queryset(self):
		sName = self.kwargs['person']
		articles = Article.objects.filter(person__subName=sName)
		if (len(articles) == 0):
			print("warning ------ POPULATING ARTICLES ------- warning")
			get_news_articles(sName)
			articles = Article.objects.filter(person__subName=sName)
		return articles







