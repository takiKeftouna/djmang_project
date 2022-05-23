
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signUp/',views.signup,name='signup'),
    path('Logout/', auth_views.LogoutView.as_view(), name='Logout'),

]