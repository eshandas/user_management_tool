from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View

from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    """
    A view for logging in a user.
    """
    template_name = 'appauth/login.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    next_page = request.GET.get('next', None)
                    if next_page:
                        return HttpResponseRedirect(next_page)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    context = {'success': False, 'message': 'User is inactive'}
            else:
                context = {'success': False, 'message': 'Incorrect username or password'}
        else:
            context = {'success': False, 'message': 'Email or password cannot be empty'}
        return render(request, self.template_name, context)


class LogoutView(View):
    """
    A view for logging out a user.
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('appauth:login'))
