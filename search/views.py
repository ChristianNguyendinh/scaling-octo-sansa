import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Artist, Article
from rest_framework import generics
from .serializers import ArtistSerializer, ArticleSerializer
from .queries import populate_news_articles, populate_artist, refresh_tweets


class InfoTestView(TemplateView):
	template_name = 'info.html'
	def get_context_data(self, **kwargs):
		context = super(InfoTestView, self).get_context_data(**kwargs)
		context['searchName'] = self.kwargs['name']
		return context

class SearchView(TemplateView):
	template_name = 'search.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

#class SubArtistDetail(generics.RetrieveAPIView):
#	lookup_field = 'subName'
#	queryset = Artist.objects.all()
#	serializer_class = ArtistSerializer

#################
## API VIEWS ####
#################
class SubArtistDetail(generics.RetrieveAPIView):
	lookup_field = 'subName'
	serializer_class = ArtistSerializer
	def get_queryset(self):
		sName = self.kwargs['subName']
		artist = Artist.objects.filter(subName=sName)
		if (len(artist) == 0):
			print("warning ------ THIS IS WHERE CALL TO POPULATE GOES! ------- warning")
			new_name = self.kwargs['subName'].replace("-", " ")
			sub_name = populate_artist(new_name)
			artist = Artist.objects.filter(subName=sub_name)
		else:
			tweet_date_delta = timezone.now() - artist[0].tweet_added_date
			if tweet_date_delta.seconds > 300: # refresh tweets if last refresh was over 5 minutes ago
				refresh_tweets(sName.lower())
		print("DONE POPULATING ARTIST")
		return artist

class ArticleDetail(generics.ListAPIView):
	serializer_class = ArticleSerializer
	def get_queryset(self):
		sName = self.kwargs['person']
		articles = Article.objects.filter(person__subName=sName)
		if (len(articles) == 0):
			print("warning ------ POPULATING ARTICLES ------- warning")
			populate_news_articles(sName)
			articles = Article.objects.filter(person__subName=sName)
		else:
			date_delta = timezone.now() - articles[0].added_date
			if date_delta.days != 0: # Refresh articles if more than a day old
				print("warning ------ REFRESHING ARTICLES ------- warning")
				# Delete old articles and replace with new ones
				Article.objects.filter(person__subName=sName).delete()
				populate_news_articles(sName)
				articles = Article.objects.filter(person__subName=sName)

		return articles







