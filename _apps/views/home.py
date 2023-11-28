from django.shortcuts import render
from datetime import date
from _apps.models.user import User, Session
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    data = {
        'mac': hex(uuid.getnode()),
        'today': date.today(),
    }
    return render(request, 'home/dashboard.html', data)
