from django.urls import path
from .views import *


urlpatterns = [
    path('login/',login_user,name='login'),
    path('register/',register_user,name='register'),
    path('logout/',logout_user,name='logout'),
    path('profile/',profile,name='profile'),
    path('change_profile_picture/',change_profile_picture,name='change_profile_picture'),
]
