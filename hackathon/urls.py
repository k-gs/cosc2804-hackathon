from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_form/', views.user_form, name='user_form'),
    path('company/', views.company, name='company'),
    path('about_us/', views.about_us, name='about_us')
]

