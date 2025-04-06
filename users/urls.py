from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.account_home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile_update/', views.update_user, name='profile_update')
]
