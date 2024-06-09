from django.urls import path

from accounts import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('user_change/<int:pk>', views.EditProfileView.as_view(), name='user_change'),
    path('profile/follow/<int:pk>', views.follow, name='follow'),
    path('profile/unfollow/<int:pk>', views.unfollow, name='unfollow'),
]
