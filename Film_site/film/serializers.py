from rest_framework import serializers
from .models import *


class ListFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = ['title','content','genre']


class DetailFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = '__all__'

class CreateFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = '__all__'