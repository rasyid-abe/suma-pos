from django.shortcuts import render
from _apps.forms.user import FormUser, FormGroup
import uuid
import hashlib

def login(request):
    data = {
        'mac': hex(uuid.getnode())
    }
    return render(request, 'auth/login.html', data)

def add_user(request):
    data = {
        'form': FormUser(),
        'act': '/add_user/',
        'btn': 'Save'
    }

    if request.POST:
        form = FormUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
            user.save()

            data['heading'] = 'Success'
            data['text'] = 'Data berhasil diinput'
            data['status'] = 'success'
        else :
            data['heading'] = 'Error'
            data['text'] = 'Data gagal diinput'
            data['status'] = 'error'

    return render(request, 'auth/user.html', data)

def add_group(request):
    data = {
        'form': FormGroup(),
        'act': '/add_group/',
        'btn': 'Save'
    }

    if request.POST:
        form = FormGroup(request.POST)
        if form.is_valid():
            form.save()

            data['heading'] = 'Success'
            data['text'] = 'Data berhasil diinput'
            data['status'] = 'success'
        else :
            data['heading'] = 'Error'
            data['text'] = 'Data gagal diinput'
            data['status'] = 'error'

    return render(request, 'auth/user.html', data)
