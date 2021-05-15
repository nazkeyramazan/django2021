from django.urls import path
from .views import *

urlpatterns = [
    path('get_token/', get_token),
    path('register/', UserRegister.as_view({'post': 'register'})),
    path('stuff/register/', UserRegister.as_view({'post': 'create_stuff'}))
]