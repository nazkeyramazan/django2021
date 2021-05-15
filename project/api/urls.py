from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path , include

from api.views_fbv import *
from api.views_cbv import  *
from api.views_viewset import *
from rest_framework import routers


urlpatterns = [
    #FBV
    path('main-categories/' , main_category_list ),
    path('main-categories/<int:main_category_id>/', main_category_detail),
    # path('book-categories/', book_category_list),
    # path('book-categories/<int:book_category_id>/', book_category_detail),

    # CBV
    path('author/', AuthorListAPIView.as_view()),
    path('author/<int:id>/', AuthorDetailAPIView.as_view()),
    path('book-categories/', BookCategoryListAPIView.as_view()),
    path('book-categories/<int:id>/', BookCategoryDetailAPIView.as_view()),

    # viewset
    path('publisher/', PublisherViewSet.as_view({'get': 'list',
                                                 'post': 'create'})),
    path('publisher/<int:id>/', PublisherViewSet.as_view({'get': 'retrieve',
                                                          'delete': 'destroy',
                                                           'put': 'update'})),
    path('auto/', AuthorViewSet.as_view({'get': 'list',
                                        'post': 'create'})),
    path('auto/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve',
                                                 'delete': 'destroy',
                                                  'put': 'update'})),
    path('books/', BookViewSet.as_view({'get': 'list',
                                                 'post': 'create'})),
    path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve',
                                                          'delete': 'destroy',
                                                          'put': 'update',
                                                 'patch': 'partial_update'})),
    path('books-detail/', BookDetailViewSet.as_view({'get': 'list',
                                        'post': 'create'})),
    path('books-detail/<int:pk>/', BookDetailViewSet.as_view({'get': 'retrieve',
                                                 'delete': 'destroy',
                                                 'put': 'update',
                                                 'patch': 'partial_update'})),
    # path('publisher/', PublisherViewSet.as_view({'GET': 'list' , 'POST' : 'create'})),
    # path('publisher/<int:id>', PublisherViewSet.as_view({'post': 'create'})),
]
