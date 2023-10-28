from django.contrib import admin
from django.urls import path
from _apps.views.auth import *
from _apps.views.home import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('add_user/', add_user, name='add_user'),
    path('add_group/', add_group, name='add_group'),
]
