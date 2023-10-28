from django.contrib import admin
from django.urls import path
from _apps.views.auth import *
from _apps.views.home import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('user/', addUser, name='user'),
]
