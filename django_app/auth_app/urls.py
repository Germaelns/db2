from django.contrib import admin
from django.urls import path, include
from auth_app import views

urlpatterns = [
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.Home.as_view(), name='home'),
    path('home/post_form/', views.post_form, name='add_post'),
    path('home/contact_form/', views.ContactFormView.as_view(), name='post_contact'),
    path('home/post_form/add_post/', views.add_post, name='add_post'),
]