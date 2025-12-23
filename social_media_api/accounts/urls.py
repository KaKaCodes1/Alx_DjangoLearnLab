from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login') ,
    path('profile/',UserProfileView.as_view(), name='user_profile'),
    path('follow/<int:user_id>', FollowUserView.as_view(),name='follow_user'),
    path('unfollow/<int:user_id>', UnfollowUserView.as_view(),name='unfollow_user'),
]