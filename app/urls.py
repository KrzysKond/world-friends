from django.urls import path

from . import views


urlpatterns=[
    path('', views.map_view, name='map'),
    path('login/', views.login_view, name='login'),
    path('singup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('friends-locations/', views.people_locations, name='friends_locations'),

    path('person/<int:person_id>/', views.person_view, name='person_detail'),
]