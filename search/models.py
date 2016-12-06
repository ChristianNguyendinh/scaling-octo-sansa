from django.db import models
from .services import get_recent_tweets, get_picture, get_name_desc

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False, unique=True)
	description = models.TextField(max_length=5000, null=True, blank=True, default="None")
	profession = models.CharField(max_length=128, null=True, blank=True, default="None")

	urls1 = models.CharField(max_length=512, null=True, blank=True)
	urls2 = models.CharField(max_length=512, null=True, blank=True)
	urls3 = models.CharField(max_length=512, null=True, blank=True)
	urls4 = models.CharField(max_length=512, null=True, blank=True)
	urls5 = models.CharField(max_length=512, null=True, blank=True)

	# uneditable
	image = models.CharField(max_length=255, null=True, blank=True, default="None")
	backupImage = models.CharField(max_length=255, null=True, blank=True, default="None")
	subName = models.CharField(max_length=128, null=False, blank=False, unique=True, default="None")
	#pageID = models.CharField(max_length=64, null=False, blank=False, unique=True, default="None")

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		# subname is name without spaces and in all lowercase. used in url.
		mylist = get_recent_tweets(self.name.replace(" ", ""))
		
		# MOVE THIS STUFF. CURRENTLY IN SAVE FOR TESTING STUFF

		self.urls1 = mylist[0]['user']['screen_name'] + "/status/" + mylist[0]['id_str']
		self.urls2 = mylist[1]['user']['screen_name'] + "/status/" + mylist[1]['id_str']
		self.urls3 = mylist[2]['user']['screen_name'] + "/status/" + mylist[2]['id_str']
		#self.urls4 = mylist[3]['user']['screen_name'] + "/status/" + mylist[3]['id_str']
		#self.urls5 = mylist[4]['user']['screen_name'] + "/status/" + mylist[4]['id_str']

		# ORDER MATTERS HERE
		if (self.subName == "None"):
			self.subName = self.name.replace(" ", "-").lower();

		if (self.description == "None" or self.profession == "None"):
			data_arr = get_name_desc(self.name)
			self.name = data_arr[0]
			self.description = data_arr[1]
			self.backupImage = data_arr[2]
			self.profession = data_arr[3]

		if (self.image == "None"):
			newImage = get_picture(self.name)
			self.image = newImage if newImage != "" else self.backupImage

		# Facebook pages too unreliable and a hassle for images. Implementing alternative
		#if (self.pageID == "None"):
		#	self.pageID = get_page_id(self.name)
		#	
		#if (self.image == "None"):
		#	newImage = get_profile_pic(self.pageID)
		#	self.image = newImage if newImage != "" else self.backupImage

		super(Artist, self).save(*args, **kwargs)

class Article(models.Model):
	articleName = models.CharField(max_length=128, null=False, blank=False, unique=True)
	articleDescription = models.TextField(max_length=5000, null=True, blank=True, default="None")
	url = models.CharField(max_length=128, null=False, blank=False, default="None")
	articleImage = models.CharField(max_length=128, null=False, blank=False, unique=True)

	person = models.ForeignKey('Artist', on_delete=models.CASCADE,)

