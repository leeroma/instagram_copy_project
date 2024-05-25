from django.urls import path

from instagram_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('profile/publication/<int:id>', views.PostPublicationView.as_view(), name='publication'),
]
