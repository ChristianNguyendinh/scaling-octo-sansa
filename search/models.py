import datetime
from django.db import models
from django.utils import timezone

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
	tweet_added_date = models.DateTimeField('date added', default= (timezone.now() - datetime.timedelta(seconds=300)));

	# uneditable
	image = models.CharField(max_length=255, null=True, blank=True, default="None")
	backupImage = models.CharField(max_length=255, null=True, blank=True, default="None")
	subName = models.CharField(max_length=128, null=False, blank=False, unique=True, default="None")
	#pageID = models.CharField(max_length=64, null=False, blank=False, unique=True, default="None")

	def __str__(self):
		return self.name

class Article(models.Model):
	articleName = models.CharField(max_length=128, null=False, blank=False, unique=True)
	articleDescription = models.TextField(max_length=5000, null=True, blank=True, default="None")
	url = models.CharField(max_length=128, null=False, blank=False, default="None")
	articleImage = models.CharField(max_length=128, null=False, blank=False, unique=True)
	added_date = models.DateTimeField('date added', default= (timezone.now() - datetime.timedelta(days=1)));
	person = models.ForeignKey('Artist', on_delete=models.CASCADE,)

