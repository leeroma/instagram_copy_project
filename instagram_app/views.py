from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from instagram_app.forms import PublicationForm, SearchForm
from instagram_app.models import Publication, Account


class IndexView(ListView):
    template_name = 'index.html'
    model = Publication
    ordering = ['-created_at']
    form_class = SearchForm

    search_value = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            followers = Account.objects.filter(follower=self.request.user)
            publications = [Publication.objects.filter(profile=follower) for follower in followers]
            context["publications"] = publications
            context['form'] = self.form_class

        return context


class ProfileView(TemplateView):
    template_name = 'accounts/user_detail.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = Account.objects.get(pk=kwargs['pk'])
        context['user'] = user
        context['publications'] = user.publications.all()
        return context


class PostPublicationView(CreateView):
    template_name = 'post_publication.html'
    form_class = PublicationForm
    model = Publication

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()
            return HttpResponseRedirect(reverse('profile', args=[publication.user.pk]))

        return render(request, self.template_name, context={'form': form})


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication_detail.html'
    context_object_name = 'publication'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchView(TemplateView):
    model = Account
    template_name = 'search.html'

    def post(self, request):
        query = request.POST['search']
        accounts = self.model.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(email__icontains=query)
        )
        if accounts:
            return render(request, self.template_name, context={'accounts': accounts})

        return render(request, self.template_name)
