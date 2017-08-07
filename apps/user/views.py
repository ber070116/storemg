from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .backend import UserBackend
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


class LoginView(LoginView):
    """View for user login"""
    template_name = 'user/login.html'

    def post(self, request, *args, **kwargs):
        """get the request sent for method post to login user"""
        username = request.POST['username']
        password = request.POST['password']

        # veiry user to login in the system
        login = UserBackend().authenticate(request, username, password)

        if login:
            return HttpResponse('si')
        else:
            return HttpResponse('no')


class test(View):
    def get(self, request):

        if request.user.is_authenticated:
            return HttpResponse('hola')
        else:
            return HttpResponse('chao')


def logoutView(request):
    logout(request)
