from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from _apps.views.auth import *
from _apps.views.home import *
from _apps.views.user import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),

    # user
    path('user/', user, name='user'),
    path('addUser/', addUser, name='addUser'),
    path('getUsers/', getUsers, name='getUsers'),
    # path('add_user/', add_user, name='add_user'),
    # path('add_group/', add_group, name='add_group'),

]
