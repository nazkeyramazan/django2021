import logging
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404, get_list_or_404

logger = logging.getLogger(__name__)

class PublisherViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated, )

    def list(self, request):
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None):
        queryset = Publisher.objects.all()
        user = get_object_or_404(queryset, id=id)
        serializer = PublisherSerializer(user)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def create(self, request):
        publisher_data = request.data
        new_publisher = Publisher.objects.create(name=publisher_data['name'],
                                                 address=publisher_data['address'],
                                                 city=publisher_data['city'],
                                                 country=publisher_data['country'],)
        new_publisher.save()
        serializer = PublisherSerializer(new_publisher)
        logger.debug(f'Created  Publisher with name: {serializer.instance}')
        logger.info(f'Created  Publisher with name : {serializer.instance}')
        return Response(serializer.data)

    def destroy(self, request, id):
        try:
            instance = Publisher.objects.get(id=id)
            instance.delete()
            logger.debug(f'Deleted Publisher with name: {instance}')
            logger.info(f'Deleted Publisher with name: {instance}')
        except Http404:
            pass
        return Response({'Publisher deleted': True})

    # , permission_classes = (IsAdminUser,)
    @action(methods=['PUT'], detail=False)
    def update(self, request, id):
        publisher = Publisher.objects.get(id=id)
        publisher.name = request.data['name']
        publisher.address = request.data['address']
        publisher.city = request.data['city']
        publisher.country = request.data['country']
        publisher.save()
        serializer = PublisherSerializer(publisher)
        logger.debug(f'Updated Publisher information: {serializer.instance}')
        logger.info(f'Updated Publisher information: {serializer.instance}')
        return Response(serializer.data)

# class BookViewSet(viewsets.ViewSet):
#     # permission_classes = (IsAuthenticated, )
#
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, id=None):
#         queryset = Book.objects.all()
#         user = get_object_or_404(queryset, id=id)
#         serializer = BookSerializer(user)
#         return Response(serializer.data)
#
#     @action(methods=['POST'], detail=False)
#     def create(self, request):
#         publisher_data = request.data
#         name = publisher_data['name']
#         category = BookCategory.objects.get(id=publisher_data['category'])
#         publisher = Publisher.objects.get(id=publisher_data['publisher'])
#         author = Author.objects.get(id=publisher_data['author'])
#         # author = self.get_object(id)
#         instance = Book.objects.create(name=name , category=category)
#
#         instance.author.add(*author)
#
#
#         new_publisher = Book.objects.create(name=name,
#                                                  description=publisher_data['description'],
#                                                  price=publisher_data['price'],
#                                                  category=category,
#                                                  publisher = publisher,
#                                                  author = author
#                                             )
#         new_publisher.save()
#         serializer = BookSerializer(new_publisher)
#         logger.debug(f'Created  Book with name: {serializer.instance}')
#         logger.info(f'Created  Book with name : {serializer.instance}')
#         return Response(serializer.data)
#
#     def destroy(self, request, id):
#         try:
#             instance = Book.objects.get(id=id)
#             instance.delete()
#             logger.debug(f'Deleted Book with name: {instance}')
#             logger.info(f'Deleted Book with name: {instance}')
#         except Http404:
#             pass
#         return Response({'Book deleted': True})
#
#     # , permission_classes = (IsAdminUser,)
#     @action(methods=['PUT'], detail=False)
#     def update(self, request, id):
#         publisher = Book.objects.get(id=id)
#         publisher.name = request.data['name']
#         publisher.address = request.data['address']
#         publisher.city = request.data['city']
#         publisher.country = request.data['country']
#         publisher.save()
#         serializer = BookSerializer(publisher)
#         logger.debug(f'Updated Book information: {serializer.instance}')
#         logger.info(f'Updated Book information: {serializer.instance}')
#         return Response(serializer.data)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookDetailViewSet(viewsets.ModelViewSet):

    queryset = BookDetail.objects.all()
    serializer_class = BookDetailSerializer

# class BookDetailViewSet(viewsets.ViewSet):
#     # permission_classes = (IsAuthenticated, )
#
#     def list(self, request):
#         queryset = BookDetail.objects.all()
#         serializer = BookDetailSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, id=None):
#         queryset = BookDetail.objects.all()
#         user = get_object_or_404(queryset, id=id)
#         serializer = BookDetailSerializer(user)
#         return Response(serializer.data)
#
#     @action(methods=['POST'], detail=False)
#     def create(self, request):
#         publisher_data = request.data
#         book =
#         new_publisher = BookDetail.objects.create(name=publisher_data['name'],
#                                                  address=publisher_data['address'],
#                                                  city=publisher_data['city'],
#                                                  country=publisher_data['country'],)
#         new_publisher.save()
#         serializer = BookDetailSerializer(new_publisher)
#         logger.debug(f'Created  Book Detail with name: {serializer.instance}')
#         logger.info(f'Created  Book Detail with name : {serializer.instance}')
#         return Response(serializer.data)
#
#     def destroy(self, request, id):
#         try:
#             instance = Publisher.objects.get(id=id)
#             instance.delete()
#             logger.debug(f'Deleted Book Detail with name: {instance}')
#             logger.info(f'Deleted Book Detail with name: {instance}')
#         except Http404:
#             pass
#             # logger.error(f'Category object cannot be deleted')
#         return Response({'Book Detail deleted': True})
#
#     # , permission_classes = (IsAdminUser,)
#     @action(methods=['PUT'], detail=False)
#     def update(self, request, id):
#         publisher = Publisher.objects.get(id=id)
#         publisher.name = request.data['name']
#         publisher.address = request.data['address']
#         publisher.city = request.data['city']
#         publisher.country = request.data['country']
#         publisher.save()
#         serializer = PublisherSerializer(publisher)
#         logger.debug(f'Updated Book Detail information: {serializer.instance}')
#         logger.info(f'Updated Book Detail information: {serializer.instance}')
#         return Response(serializer.data)