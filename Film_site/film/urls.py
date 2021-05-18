from django.urls import path
from .views import *
urlpatterns = [
    path('',Glavnaya.as_view(),name="Glav"),
    path('movie/<str:slug>',SingleMovie.as_view(),name="Single_movie"),
    path('Films_list',MovieList.as_view(),name="List_movie"),
    path('Registration',Registration.as_view(),name="registration"),
    path('login',user_login,name="login"),
    path('logout',user_logout,name="logout"),
    path('actor/<str:slug>',Single_actor.as_view(),name="Single_actor"),
    path('Films_list/<str:slug>',By_genre.as_view(),name="By_genre"),
    path('actors', ActorsList.as_view(),name="Actors_list"),
    path('search',Search, name="search"),
    path('filter', Filter.as_view(),name="filter"),
    path('actor_filter',Actor_Filter.as_view(),name="actor_filter"),
    path('New_film',New_Films.as_view(),name='New_film')
]