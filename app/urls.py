from django.urls import path

from . import views


urlpatterns=[
    path('', views.map_view, name='map'),
    path('login/', views.login_view, name='login'),
    path('singup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),

    path('friends-locations/', views.people_locations, name='friends_locations'),

]