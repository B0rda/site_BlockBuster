from django.contrib import admin
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ('name',)}


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','country','photo')
    prepopulated_fields = {"slug": ('name',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug":('title',)}


class FilmsAdmin(admin.ModelAdmin):
    list_display = ('pk','title','release_date','during','age_rating')
    prepopulated_fields = {"slug": ('title',)}

class AgeAdmin(admin.ModelAdmin):
    list_display = ('age_rating',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'movie')

admin.site.register(Country,CountryAdmin)
admin.site.register(Actor,ActorAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(film,FilmsAdmin)
admin.site.register(AgeRating,AgeAdmin)
admin.site.register(Review,ReviewAdmin)
# Register your models here.
