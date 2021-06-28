from django.urls import path
from .views import *
urlpatterns = [
    path('all_film',ApiFilmAll.as_view()),
    path('detail/<int:pk>',ApiFilmDetail.as_view()),
    path('create_film',ApiFilmCreate.as_view())
]