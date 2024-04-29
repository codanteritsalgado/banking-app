from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path('',        UserViewSet.as_view({'get': 'index'}), name='user-index'),
    path('list/',   UserViewSet.as_view({'get': 'list_users'}), name='list-users'),
    path('create/', UserViewSet.as_view({'post': 'create_user'}), name='create-user'),
    path('profile/',UserViewSet.as_view({'get': 'user_profile'}), name='user-profile'),
    path('login/',  UserViewSet.as_view({'post': 'login'}), name='login'),
    path('logout/', UserViewSet.as_view({'post': 'logout'}), name='logout'),
]
