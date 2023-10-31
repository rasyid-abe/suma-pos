from django.shortcuts import render
from _apps.forms.user import FormUser, FormGroup
from _apps.models.user import User
import uuid
import bcrypt

def login(request):
    data = {}
    redirect = 'auth/login.html'
    if request.POST:
        user = request.POST
        if User.objects.filter(username=user['username']).exists():
            row = User.objects.filter(username=user['username'])[0]
            hash = row.password
            pwd = user['password'].encode('utf-8')
            result = bcrypt.checkpw(pwd, hash)
            if result:
                if row.is_active:

                    redirect = 'auth/user.html'


                else:
                    data['heading'] = 'Error'
                    data['text'] = 'Akun anda tidak aktif.'
                    data['status'] = 'error'

            else:
                data['heading'] = 'Error'
                data['text'] = 'Password Salah'
                data['status'] = 'error'

        else :
            data['heading'] = 'Error'
            data['text'] = 'User tidak terdaftar'
            data['status'] = 'error'

    # data = {
    #     'mac': hex(uuid.getnode())
    # }
    return render(request, redirect, data)

def add_user(request):
    data = {
        'form': FormUser(),
        'act': '/add_user/',
        'btn': 'Save'
    }

    if request.POST:
        form = FormUser(request.POST)
        if form.is_valid():
            salt = bcrypt.gensalt()

            user = form.save(commit=False)
            user.password = bcrypt.hashpw(user.username.encode('utf-8'), salt)
            # import pdb; pdb.set_trace()
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
