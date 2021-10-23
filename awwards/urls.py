from django.urls import path
from .import views


urlpatterns =[

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.userPage,name='user-page'),
    path('user/',views.logoutUser,name='logout'),
    path('',views.post,name='auth'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.project_upload, name='post_view'),


]