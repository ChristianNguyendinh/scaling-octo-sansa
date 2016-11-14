from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Artist
from rest_framework import generics
from .serializers import ArtistSerializer
from .services import get_recent_tweets

####################
## REAL VIEWS ######
####################

class InfoTestView(TemplateView):
	template_name = 'info.html'
	def get_context_data(self, **kwargs):
		context = super(InfoTestView, self).get_context_data(**kwargs)
		context['searchName'] = self.kwargs['name']
		return context


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
			#self.populate_artist(sName)
			print("warning ------ THIS IS WHERE CALL TO POPULATE GOES! ------- warning")
			newName = self.kwargs['subName'].replace("-", " ")
			a = Artist(name=newName)
			a.save()
			artist = Artist.objects.filter(subName=a.subName)
		return artist

	def populate_artist(self, sub):
		get_recent_tweets("asdf")

