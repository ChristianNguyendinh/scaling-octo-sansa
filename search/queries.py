import urllib, requests, json, sys
from requests_oauthlib import OAuth1
from django.conf import settings
from .models import Artist, Article

# PUT multiple articles in the database
def get_news_articles(search_name):
	headers = {"Ocp-Apim-Subscription-Key": settings.BING_NEWS_API_KEY}
	q = urllib.parse.quote(search_name)
	url = "https://api.cognitive.microsoft.com/bing/v5.0/news/search?q=" + q + "&originalImg=true&mkt=en-us"
	
	r = requests.get(url, headers=headers)
	print(json.dumps(r.json(), indent=4))

	articleList = r.json()['value'];
	i = 1
	for article in articleList :
		if (i > 3):
			break
		#try:
		related_artist = Artist.objects.get(subName=search_name)
		a = Article(articleName=article['name'], articleDescription=article['description'], 
			url=article['url'], articleImage=article['image']['contentUrl'], person=related_artist)
		a.save()
			#print(article['name'])
			#print(article['description'])
			#print(article['url'])
			#print(article['image']['contentUrl'])

		#except:
		#	print("Error trying to save/get an article for " + str(q))
		#	print(sys.exc_info()[0])
		#	pass

		#finally:
		i += 1