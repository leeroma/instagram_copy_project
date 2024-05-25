from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from instagram_app.forms import PublicationForm
from instagram_app.models import Profile, Publication, Account


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileView(TemplateView):
    template_name = 'main/profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        account = Account.objects.get(pk=self.kwargs['id'])
        profile = Profile.objects.get(user_id=account.id)
        publication = Publication.objects.filter(profile_id=profile.id)

        context['publications'] = publication
        context['posts'] = publication.count()
        context['followers'] = profile.follower.count()
        context['following'] = Profile.objects.filter(follower=account.id).count()
        context['profile'] = profile
        return context


class PostPublicationView(CreateView):
    template_name = 'main/post_publication.html'
    form_class = PublicationForm
    model = Publication

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        profile = Profile.objects.get(user_id=kwargs.get('id'))
        if form.is_valid():
            publication = form.save(commit=False)
            publication.profile = profile
            publication.save()
            return HttpResponseRedirect(reverse('profile', args=[publication.profile.id]))

        return render(request, self.template_name, context={'form': form})
