from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from accounts.forms import AccountCreationForm
from instagram_app.models import Profile


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


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = AccountCreationForm
    success_url = 'index'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(user=user)
            return redirect('index')

        context = {'form': form}
        return render(request, self.template_name, context=context)
