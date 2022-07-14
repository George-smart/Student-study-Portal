from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up', SignUp.as_view(), name='signup'),
    path('signin', Signin, name='login'),
    path('logout', Signout, name='logout'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('create_profile', ProfileCreation.as_view(), name='create_profile'),
    path('update_profile/<int:pk>', UpdateProfile.as_view(), name='update_profile')

]
