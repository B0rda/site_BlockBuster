from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import os
from pathlib import Path


def photo_path(instance,filename):
    return "actor/"+instance.slug+"/"+filename

def photo_film_path(instance,filename):
    return "film/"+instance.slug+"/"+filename

class Genre(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30,unique=True)
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("By_genre", kwargs={"slug":self.slug})

class AgeRating(models.Model):
    age_rating = models.CharField(max_length=10)
    def __str__(self):
        return self.age_rating


class Country(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40,unique=True)
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70,unique=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    country = models.ForeignKey(Country,on_delete=models.PROTECT)
    photo = models.ImageField(upload_to=photo_path)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("Single_actor",kwargs={"slug":self.slug})



class film(models.Model):
    title = models.CharField(max_length=130)
    slug = models.SlugField(max_length=130,unique=True)
    photo = models.ImageField(upload_to=photo_film_path,max_length=1000)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    content = models.TextField(max_length=600,blank=True)
    actors = models.ManyToManyField(Actor,related_name='actors')
    direc = models.ManyToManyField(Actor,related_name='directors')
    genre = models.ManyToManyField(Genre,blank=True)
    during = models.SlugField(max_length= 10)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    age_rating = models.ForeignKey(AgeRating,on_delete=models.PROTECT)
    views = models.IntegerField(default=0)
    silka = models.FileField(upload_to=photo_film_path)
    time_add = models.DateTimeField(auto_now_add=True)
    trailer = models.CharField(max_length=300,blank=True)
    country = models.ManyToManyField(Country,related_name='country')
    def get_absolute_url(self):
        return reverse("Single_movie",kwargs={"slug":self.slug})
    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=70,blank=True)
    content = models.TextField(max_length=700)
    write_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    movie = models.ForeignKey(film,on_delete=models.CASCADE,default=1)