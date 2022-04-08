from .views import login,logout,signup,house
from django.urls import path

urlpatterns=[
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('logout',logout,name='logout'),
    path('',house,name='house')
]