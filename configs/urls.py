from django.contrib import admin
from django.urls import path
from _apps.views.auth import *
from _apps.views.main import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
]
