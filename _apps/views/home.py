from django.shortcuts import render
import uuid

def home(request):
    data = {
        'mac': hex(uuid.getnode())
    }
    return render(request, 'dashboard/home.html', data)
