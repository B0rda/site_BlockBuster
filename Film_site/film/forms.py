from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Review
from django.forms import ModelForm

class NewUser(UserCreationForm):
    username = forms.CharField(label="Имя",widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password1 = forms.CharField(label = "Пароль",widget=forms.PasswordInput(attrs={"placeholder":"koko2"}))
    password2 = forms.CharField(label = "Повторите пароль",widget=forms.PasswordInput(attrs={"placeholder":"ururu"}))
    email = forms.CharField(label= "Почта",widget=forms.EmailInput(attrs={"placeholder":'username@mail.ru'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginUser(AuthenticationForm):
    username = forms.CharField(max_length=254,label="Имя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class FormReview(forms.ModelForm):
    title = forms.CharField(label="Заголовок:",widget=forms.TextInput(attrs={"id":"title_review"}))
    content = forms.CharField(label="Комментарий:",widget=forms.Textarea(attrs={"id":"content_review"}))
    class Meta:
        model = Review
        fields = ['title','content']