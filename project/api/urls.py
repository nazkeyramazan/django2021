from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from api.views_fbv import *
urlpatterns = [
    path('main-categories/' , main_category_list ),
    path('main-categories/<int:main_category_id>/', main_category_detail),
    path('book-categories/', book_category_list),
    path('book-categories/<int:book_category_id>/', book_category_detail),

]