from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from instagram_app.forms import PublicationForm, SearchForm
from instagram_app.models import Publication, Account, Comment


class IndexView(ListView):
    template_name = 'index.html'
    model = Publication
    form_class = SearchForm

    search_value = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            publications = Publication.objects.filter(user__follower=self.request.user).order_by('-created_at')
            context["publications"] = publications
            context['search_form'] = self.form_class

        return context


class ProfileView(TemplateView):
    template_name = 'accounts/user_detail.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = Account.objects.get(pk=kwargs['pk'])
        context['user'] = user
        context['publications'] = user.publications.all().order_by('-created_at')
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


class FollowersView(TemplateView):
    template_name = 'accounts/followers.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.model.objects.get(pk=kwargs['pk'])
        context['followers'] = user.get_all_followers
        return context


class FollowsView(TemplateView):
    template_name = 'accounts/follows.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.model.objects.get(pk=kwargs['pk'])
        context['follows'] = user.get_all_follows
        return context


def like_view(request, **kwargs):
    publication = Publication.objects.get(pk=kwargs['pk'])
    publication.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_like_view(request, **kwargs):
    publication = Publication.objects.get(pk=kwargs['pk'])
    publication.likes.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CommentCreateView(CreateView):
    model = Comment

    def post(self, request, *args, **kwargs):
        publication = Publication.objects.get(pk=kwargs['pk'])
        if request.POST['text']:
            comment = self.model.objects.create(
                publication=publication,
                user=request.user,
                text=request.POST['text']
            )
            comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
