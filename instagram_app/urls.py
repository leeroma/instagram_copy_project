from django.urls import path

from instagram_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/publication/<int:pk>', views.PostPublicationView.as_view(), name='post_publication'),
    path('publication/<int:pk>', views.PublicationDetailView.as_view(), name='publication'),
    path('search', views.SearchView.as_view(), name='search'),
    path('profile/followers/<int:pk>', views.FollowersView.as_view(), name='followers'),
    path('profile/follows/<int:pk>', views.FollowsView.as_view(), name='follows'),
    path('publication/like/<int:pk>', views.like_view, name='like'),
    path('publication/remove_like/<int:pk>', views.remove_like_view, name='remove_like'),
]
