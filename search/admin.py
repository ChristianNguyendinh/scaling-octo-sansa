from django.contrib import admin
from .models import Artist

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name']

admin.site.register(Artist, ArtistAdmin)