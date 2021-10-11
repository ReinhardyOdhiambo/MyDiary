
from django.urls import path
from . import views


urlpatterns = [
  path('', views.landing, name='landing'),
  path('newentry', views.newentry, name='newentry'),
  
  path('search' , views.search, name='search'),
  path('viewentry' , views.viewentry, name='viewentry'),
  path('home/' , views.home, name='home'),
  path('landing/' , views.landing, name='landing'),
  path('settings/' , views.settings, name='settings'),
  path('profile/' , views.profile, name='profile'),
  path('login/' , views.login, name='login'),
  path('signup/' , views.signup, name='signup'),
  path('logout/' , views.logout, name='logout'),

  ]
