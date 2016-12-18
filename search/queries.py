import urllib, requests, json, sys
from requests_oauthlib import OAuth1
from django.conf import settings
from django.utils import timezone
from .models import Artist, Article
from .services import get_news_articles, get_recent_tweets, get_picture, get_name_desc

# PUT multiple articles in the database
def populate_news_articles(search_name):
	articleList = get_news_articles(search_name);

	i = 1
	for article in articleList : # get three articles
		if (i > 3):
			break

		if 'image' not in article: # want an article with a picture
			continue

		related_artist = Artist.objects.get(subName=search_name)
		# create and save the new article objects
		a = Article(articleName=article['name'], articleDescription=article['description'], 
			url=article['url'], articleImage=article['image']['contentUrl'], added_date=timezone.now(), person=related_artist)
		a.save()
		i += 1

def populate_artist(search_name):
	a = Artist(name=search_name)

	# Get tweets
	tweet_list = get_recent_tweets(a.name.replace(" ", ""))

	a.urls1 = tweet_list[0]['user']['screen_name'] + "/status/" + tweet_list[0]['id_str']
	a.urls2 = tweet_list[1]['user']['screen_name'] + "/status/" + tweet_list[1]['id_str']
	a.urls3 = tweet_list[2]['user']['screen_name'] + "/status/" + tweet_list[2]['id_str']
	# Let's stick to 3 for now
	#self.urls4 = tweet_list[3]['user']['screen_name'] + "/status/" + tweet_list[3]['id_str']
	#self.urls5 = tweet_list[4]['user']['screen_name'] + "/status/" + tweet_list[4]['id_str']

	# ORDER MATTERS HERE
	if (a.subName == "None"):
		a.subName = a.name.replace(" ", "-").lower();

	# Get description info
	if (a.description == "None" or a.profession == "None"):
		data_arr = get_name_desc(a.name)
		a.name = data_arr[0]
		a.description = data_arr[1]
		a.backupImage = data_arr[2]
		a.profession = data_arr[3]

	# Get images
	if (a.image == "None"):
		newImage = get_picture(a.name)
		a.image = newImage if newImage != "" else a.backupImage

	a.save()

	# return the sub name for ease of filtering right after
	return a.subName

def refresh_tweets(search_name):
	a = Artist.objects.get(subName=search_name)

	# Get tweets
	tweet_list = get_recent_tweets(a.name.replace(" ", ""))

	a.urls1 = tweet_list[0]['user']['screen_name'] + "/status/" + tweet_list[0]['id_str']
	a.urls2 = tweet_list[1]['user']['screen_name'] + "/status/" + tweet_list[1]['id_str']
	a.urls3 = tweet_list[2]['user']['screen_name'] + "/status/" + tweet_list[2]['id_str']

	a.save()




