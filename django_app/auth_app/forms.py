from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'image', 'text', 'author']


class ContactForm(forms.Form):
    name_sender = forms.CharField(max_length=100 , label="Введите ваше имя")
    message = forms.CharField(widget=forms.Textarea ,label = "Сообщение" )
    sender = forms.EmailField(label = "Введите ваш емейл!" )


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user