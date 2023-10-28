from django.shortcuts import render
from _apps.forms.user import FormUser
import uuid

def login(request):
    data = {
        'mac': hex(uuid.getnode())
    }
    return render(request, 'auth/login.html', data)

def addUser(request):
    form = FormUser

    data = {
        'form': form,
    }

    return render(request, 'auth/user.html', data)
