from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path , include

from api.views_fbv import *
from api.views_cbv import  *
from api.views_viewset import PublisherViewSet
from rest_framework import routers

#
router = routers.SimpleRouter()
router.register('publisher', PublisherViewSet, basename='api')

urlpatterns = [
    path('', include(router.urls)),
    path('main-categories/' , main_category_list ),
    path('main-categories/<int:main_category_id>/', main_category_detail),
    path('book-categories/', book_category_list),
    path('book-categories/<int:book_category_id>/', book_category_detail),

    path('author/', AuthorListAPIView.as_view()),
    path('author/<int:id>/', AuthorDetailAPIView.as_view()),

    # path('publisher/', PublisherViewSet.as_view({'GET': 'list' , 'POST' : 'create'})),
    # path('publisher/<int:id>', PublisherViewSet.as_view({'post': 'create'})),
]
