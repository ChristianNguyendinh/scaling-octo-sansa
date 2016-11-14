import urllib, requests, json
from requests_oauthlib import OAuth1

def get_name_desc(search_name):
	url = 'https://kgsearch.googleapis.com/v1/entities:search'
	key = "<your google api key>"
	#query = "kanye west"
	query = search_name
	fq = urllib.parse.quote(query)
	param1 = "?query="
	param2 = "&limit=1&indent=True&key="
	r = requests.get(url + param1 + fq + param2 + key)

	return_array = ['fill', 'me', 'up'];

	return_array[0] = r.json()['itemListElement'][0]['result']['name']
	return_array[1] = r.json()['itemListElement'][0]['result']['detailedDescription']['articleBody']
	return_array[2] = r.json()['itemListElement'][0]['result']['image']['contentUrl']

	return return_array

def get_recent_tweets(search_name):
	# Comment out
	query = "#" + search_name
	query_string = urllib.parse.quote(query)
	print(query_string)

	# Move to settings
	oauth = OAuth1('your twitter oauth credentials');
	
	url = "https://api.twitter.com/1.1/search/tweets.json?q=" + query_string
	r = requests.get(url, auth=oauth)
	#print(json.dumps(r.json(), indent=4))

	#j = json.loads(json.dumps(r.json()))

	#print(r.json()['statuses'][0]['text'])
	return r.json()['statuses'][:5]

def get_page_id(search_name):
	url = "https://graph.facebook.com/"
	user_token = "<your facebook user access token>"

	query = search_name
	fq = urllib.parse.quote(query)
	param1 = "search?q="
	param2 = "&type=page&access_token="

	r0 = requests.get(url + param1 + fq + param2 + user_token);
	#print(json.dumps(r0.json(), indent=4))
	print(str(r0.json()['data'][0]['id']))
	return str(r0.json()['data'][0]['id'])

def get_profile_pic(page_id):
	url = "https://graph.facebook.com/"
	app_token = "<your facebook app access_token>"

	#replace with page id - Did it...
	#ids = "19614945368"
	params = "?fields=photos&access_token="
	try:
		r = requests.get(url + page_id + params + app_token)
		pid = r.json()['photos']['data'][0]['id']

		r2 = requests.get(url + pid + "?fields=images&access_token=" + app_token)
		imgsrc = r2.json()['images'][0]['source']

		return str(imgsrc)
	except:
		return ""



