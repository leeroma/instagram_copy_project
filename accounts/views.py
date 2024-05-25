from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

        context = {'message': 'Invalid username or password'}

        return render(request, self.template_name, context=context)
