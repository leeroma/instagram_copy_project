from django.urls import path

from instagram_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/publication/<int:pk>', views.PostPublicationView.as_view(), name='post_publication'),
    path('publication/<int:pk>', views.PublicationDetailView.as_view(), name='publication'),
    path('search', views.SearchView.as_view(), name='search'),
]
