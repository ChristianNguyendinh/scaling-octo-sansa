from django.contrib import admin
from .models import Artist, Article

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name']

admin.site.register(Artist, ArtistAdmin)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('articleName',)
	search_fields = ['articleName']

admin.site.register(Article, ArticleAdmin)