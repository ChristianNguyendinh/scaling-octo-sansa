from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'search'
urlpatterns = [
	url(r'^info/(?P<name>[\w-]+)/$', views.InfoTestView.as_view()),

	#json calls
	url(r'^api/(?P<subName>[\w-]+)/$', views.SubArtistDetail.as_view()),
	url(r'^api/articles/(?P<person>[\w-]+)/$', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)