import re
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse
from _apps.forms.user import FormUser, FormGroup


@login_required(login_url=settings.LOGIN_URL)
def profile(request):
    data = {
        'mac': 'slkdfj'
    }
    return render(request, 'user/profile.html', data)

@login_required(login_url=settings.LOGIN_URL)
def user(request):
    data = {
        'users': 'abc',
    }
    return render(request, 'user/user.html', data)

def extract_(query_dict, param):
    dictionary = {}
    regex = re.compile('%s\[([\w\d_]+)\]' % param)
    for key, value in query_dict.items():
        match = regex.match(key)
        if match:
            inner_key = match.group(1)
            regex_sec = re.compile('%s\[%s\]\[([\w\d_]+)\]' % (param, inner_key))
            match_second = regex_sec.match(key)
            if match_second:
                dictionary[inner_key] = extract_(query_dict, '%s\[%s\]' % (param, inner_key))
            else:
                dictionary[inner_key] = value

    return dictionary

def getUsers(request):
    if request.method == 'GET':
        draw = int(request.GET['draw'])
        start = int(request.GET['start'])
        length = int(request.GET['length'])
        order = extract_(request.GET, 'order')
        search = extract_(request.GET, 'search')['value']

        dir = None
        col = None
        for o in order.values():
            dir = o['dir']
            col = int(o['column'])

        list_columns = {
            0:'username',
            1:'email'
        }

        by = '-' if dir != 'asc' else ''
        if search != '':
            if col == 0 and dir == 'asc' :
                users = User.objects.all() \
                    .filter( \
                    Q(username__contains=search) | \
                    Q(email__contains=search) \
                    )[start:length].values()
            else:
                users = User.objects.all().order_by(by + list_columns[col]) \
                    .filter( \
                    Q(username__contains=search) | \
                    Q(email__contains=search) \
                    )[start:length].values()
        else:
            if col == 0 and dir == 'asc' :
                users = User.objects.all()[start:length].values()
            else:
                users = User.objects.all().order_by(by + list_columns[col])[start:length].values()

        total = User.objects.all().count()
        return JsonResponse({
            "draw": draw,
            "recordsTotal": total,
            "recordsFiltered": total,
            "data": list(users)
        })

@login_required(login_url=settings.LOGIN_URL)
def addUser(request):
    data = {
        'form': FormUser(),
        'act': '/addUser/',
        'btn': 'Save'
    }

    if request.POST:
        msg = ''
        form = FormUser(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.save()
            except Exception as e:
                msg = e


            data['heading'] = 'Success'
            data['text'] = 'Insert success'
            data['status'] = 'success'
            data['time'] = 3000
        else :
            data['heading'] = 'Error'
            data['text'] = form.errors
            data['status'] = 'error'
            data['time'] = 10000

        print(form.errors)

    return render(request, 'user/addUser.html', data)
