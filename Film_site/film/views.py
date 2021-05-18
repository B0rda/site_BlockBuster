from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from .models import *
from .forms import NewUser,LoginUser, FormReview
from django.contrib.auth import login,logout
from django.contrib import messages
from django.db.models import F,Q
from datetime import datetime

def user_login(request):
    if request.method == 'POST':
        form = LoginUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        else:
            error = form.non_field_errors
            form = LoginUser()
            return render(request, "login.html", {"form": form, "error": error})
    else:
        form = LoginUser()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/")

class Glavnaya(ListView):
    template_name = 'index.html'
    context_object_name = 'films'

    def get_queryset(self):
        return film.objects.order_by("-release_date")[:12]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['populars'] = film.objects.order_by("-views")[:12]
        return context

    def post(self,request):
        return user_login(request)


class Registration(CreateView):
    form_class = NewUser
    template_name = "registration.html"
    def form_valid(self, form):
        form.save()
        return redirect("/")
    def form_invalid(self, form):
        print(self.request.path_info)
        return redirect("/")


class MovieList(ListView):
    model = film
    template_name = 'filmslist.html'
    context_object_name = 'films'
    paginate_by = 8
    def get_context_data(self,**kwargs):
        context = super().get_context_data()
        context["title"] = "Список фильмов"
        return context
    def post(self,request,**kwargs):
        return user_login(request)

class SingleMovie(DetailView):
    model = film
    template_name = 'filmsingle.html'
    context_object_name = 'single'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["review"] = Review.objects.filter(movie__slug = self.kwargs["slug"])
        context["form_review"] = FormReview()
        self.object.views = F('views')+1
        self.object.save()
        self.object.refresh_from_db()
        return context
    def post(self,request,**kwargs):
        if "title" in request.POST:
            form = FormReview(request.POST)
            z = film.objects.get(slug=self.kwargs["slug"])
            if form.is_valid():
                baza = form.save(commit=False)
                baza.user = (request.user)
                baza.movie_id = z.pk
                baza.save()
            else:
                return redirect(request.path_info)
            return redirect(request.path_info)
        else:
            return user_login(request)



class ActorsList(ListView):
    model = Actor
    template_name = "actorslist.html"
    context_object_name = 'actorslist'
    paginate_by = 10
    def post(self,request,**kwargs):
        return user_login(request)
    def get_context_data(self,**kwargs):
        context= super(ActorsList, self).get_context_data()
        context['title'] = 'Список актеров'
        return context

class Single_actor(DetailView):
    model = Actor
    template_name = 'actorsingle.html'
    context_object_name = 'actor_single'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = film.objects.filter(actors__slug = self.kwargs["slug"]).order_by("-release_date")
        context['direct'] = film.objects.filter(direc__slug = self.kwargs["slug"]).order_by("-release_date")
        context['all'] = context['films'].count()+context['direct'].count()
        return context
    def post(self,request,**kwargs):
        return user_login(request)


class By_genre(ListView):
    template_name = 'filmslist.html'
    context_object_name = "films"
    paginate_by = 8
    def get_queryset(self, **kwargs):
        return film.objects.filter(genre__slug=self.kwargs["slug"])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Genre.objects.get(slug = self.kwargs['slug'])
        return context
    def post(self,request,**kwargs):
        return user_login(request)


def Search(request):
    if request.POST:
        return user_login(request)
    if request.GET["select"] == 'actors':
        context = Actor.objects.filter(name__icontains = request.GET["search_field"])
        context1 = "actorslist"
        template_name = 'actorslist.html'
        print(request.path)
    else:
        context = film.objects.filter(title__icontains = request.GET["search_field"])
        context1 = "films"
        template_name = 'filmslist.html'
    return render(request,template_name,{context1:context})


class Filter(ListView):
    template_name = 'filmslist.html'
    paginate_by = 8
    context_object_name = 'films'
    def get_queryset(self):
        if 'genres' not in self.request.GET:
            genres = Q(genre__id__icontains="")
        else:
            genres = Q()
            for i in self.request.GET.getlist('genres'):
                genres = genres | Q(genre__slug__icontains=i)
        if 'countrys' not in self.request.GET:
            countrys = Q(country__slug__icontains="")
        else:
            countrys = Q()
            for i in self.request.GET.getlist('countrys'):
                countrys = countrys | Q(country__slug__icontains=i)
        if 'age_rating' not in self.request.GET:
            age_rating = Q(age_rating__id__icontains="")
        else:
            age_rating = Q()
            for i in self.request.GET.getlist('age_rating'):
                age_rating = age_rating | Q(age_rating__id__icontains=i)
        return film.objects.filter(genres).filter(countrys).filter(age_rating).filter(release_date__year__gte = self.request.GET.get('date1'), release_date__year__lte=self.request.GET.get('date2'),rating__gte=self.request.GET.get('mark')).distinct()
    def get_context_data(self, **kwargs):
        context = super(Filter, self).get_context_data()
        context['title'] = "Фильтр фильмов"
        context['page'] = f"{self.request.META['QUERY_STRING']}&"
        return context
    def post(self,request,**kwargs):
        return user_login(request)


class Actor_Filter(ListView):
    template_name = 'actorslist.html'
    context_object_name = 'actorslist'
    paginate_by = 10
    def get_queryset(self):
        if 'countrys' not in self.request.GET:
            countrys = Q(country__slug__icontains="")
        else:
            countrys = Q()
            for i in self.request.GET.getlist('countrys'):
                countrys = countrys | Q(country__slug__icontains=i)
        return Actor.objects.filter(countrys).filter(date_of_birth__year__gte = self.request.GET.get('date1'), date_of_birth__year__lte=self.request.GET.get('date2'))
    def get_context_data(self, **kwargs):
        context = super(Actor_Filter, self).get_context_data()
        context['title'] = "Фильтр актеров"
        context['page'] = f"{self.request.META['QUERY_STRING']}&"
        return context
    def post(self,request,**kwargs):
        return user_login(request)

class New_Films(ListView):
    template_name = "filmslist.html"
    context_object_name = "films"
    paginate_by = 8
    def get_queryset(self):
        return film.objects.filter(release_date__year = datetime.now().year)
    def post(self,request,**kwargs):
        return user_login(request)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(New_Films, self).get_context_data()
        context['title'] = "Новинки"
        return context