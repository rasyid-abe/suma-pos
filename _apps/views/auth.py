from django.shortcuts import render
import uuid

def login(request):
    data = {
        'mac': hex(uuid.getnode())
    }
    return render(request, 'auth/login.html', data)
