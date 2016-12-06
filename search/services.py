import urllib, requests, json
from requests_oauthlib import OAuth1
from django.conf import settings

def get_name_desc(search_name):
	url = 'https://kgsearch.googleapis.com/v1/entities:search'
	query = search_name
	fq = urllib.parse.quote(query)
	param1 = "?query="
	param2 = "&limit=1&indent=True&key="
	r = requests.get(url + param1 + fq + param2 + settings.GOOGLE_API_KEY)

	return_array = ['please', 'choke', 'me', 'daddy'];

	return_array[0] = r.json()['itemListElement'][0]['result']['name']
	return_array[1] = r.json()['itemListElement'][0]['result']['detailedDescription']['articleBody']
	return_array[2] = r.json()['itemListElement'][0]['result']['image']['contentUrl']
	return_array[3] = r.json()['itemListElement'][0]['result']['description']

	return return_array

def get_recent_tweets(search_name):

	query = "#" + search_name
	query_string = urllib.parse.quote(query)
	#print(query_string)

	oauth = OAuth1(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_COMSUMER_SECRET
		, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_SECRET)
	
	url = "https://api.twitter.com/1.1/search/tweets.json?q=" + query_string
	r = requests.get(url, auth=oauth)
	#print(json.dumps(r.json(), indent=4))

	#j = json.loads(json.dumps(r.json()))

	#print(r.json()['statuses'][0]['text'])
	return r.json()['statuses'][:5]

def get_picture(search_name):
	headers = {"Authorization": "Client-ID " + settings.IMGUR_CLIENT_ID}
	q = urllib.parse.quote(search_name.lower())
	url = "https://api.imgur.com/3/gallery/search/top/year/1?q_exactly=" + q

	print(url)
	r = requests.get(url, headers=headers)
	#print(r.json()['data'][0])

	data = r.json()['data']
	most_popular = None
	curr_max = 0

	for image in data:
		if image['section'] == "Celebs":
			if image['ups'] > curr_max:
				curr_max = image['ups']
				most_popular = image

	return "" if most_popular == None else most_popular['link']
	#print(most_popular['link'])

# ---------------------------------------------------------------
# Searching facebook pages for a profile pic was bad because the
# key had to be regenerated frequently, and it was unreliable.
# Currently commenting these methods out to switch to another 
# source for finding pictures
# ---------------------------------------------------------------

# def get_page_id(search_name):
# 	url = "https://graph.facebook.com/"
# 	query = search_name
# 	fq = urllib.parse.quote(query)
# 	param1 = "search?q="
# 	param2 = "&type=page&access_token="

# 	r0 = requests.get(url + param1 + fq + param2 + settings.FACEBOOK_USER_TOKEN);
# 	#print(json.dumps(r0.json(), indent=4))
# 	print(str(r0.json()['data'][0]['id']))
# 	return str(r0.json()['data'][0]['id'])

# def get_profile_pic(page_id):
# 	url = "https://graph.facebook.com/"
# 	app_token = settings.FACEBOOK_APP_TOKEN

# 	#replace with page id - Did it...
# 	#ids = "19614945368"
# 	params = "?fields=photos&access_token="
# 	try:
# 		r = requests.get(url + page_id + params + app_token)
# 		pid = r.json()['photos']['data'][0]['id']

# 		r2 = requests.get(url + pid + "?fields=images&access_token=" + app_token)
# 		imgsrc = r2.json()['images'][0]['source']

# 		return str(imgsrc)
# 	except:
# 		return ""




