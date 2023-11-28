from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
)
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode
from django.shortcuts import resolve_url
from django.conf import settings
from django.http import HttpResponseRedirect
from _apps.forms.auth import AuthForm

def login(request):
    redirect_to = request.POST.get(
        REDIRECT_FIELD_NAME,
        request.GET.get(REDIRECT_FIELD_NAME, '')
    )

    data = {
        'form': AuthForm(),
        'act': '/login/',
        'btn': 'Login',
    }
    redirect = 'auth/login.html'

    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():

            if not url_has_allowed_host_and_scheme(url=redirect_to, allowed_hosts=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            data['heading'] = 'Error'
            data['status'] = 'error'

            exists = User.objects.filter(username=form['username'].value())
            if len(exists) > 0:
                user = authenticate(username=form['username'].value(), password=form['password'].value())
                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
                        return HttpResponseRedirect("/home/")
                    else:
                        data['text'] = 'Password salah!'
                else:
                    data['text'] = 'Password salah!'
            else:
                data['text'] = 'Akun anda tidak terdaftar!'

    return render(request, redirect, data)
