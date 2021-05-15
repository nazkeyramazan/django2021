import logging

from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from api.serializers import *
from api.models import *
from api.managers import BookManager , PublisherManager , BookDetailManager , AuthorManager

from rest_framework.permissions import IsAdminUser,IsAuthenticated
logger = logging.getLogger(__name__)

class AuthorListAPIView(APIView):
    def get(self,request):
        author = Author.objects.all()
        # author = AuthorManager.all()
        serializer = AuthorModelSerializer(author, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = AuthorModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Created Author with name: {serializer.instance}')
            logger.info(f'Created Author with name : {serializer.instance}')
            return Response (serializer.data , status=status.HTTP_201_CREATED)


        return Response ({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuthorDetailAPIView(APIView):
    def get_object(self , id):
        try:
            return Author.objects.get(id = id)
        except Author.DoesNotExist as e:
            return Response({'Error':str(e)})

    def get(self, request , id):
        author = self.get_object(id)
        serializer = AuthorModelSerializer(author)
        return Response(serializer.data)

    def put(self, request , id):
        author = self.get_object(id)
        serializer = AuthorModelSerializer(instance=author , data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Updated Author with name: {serializer.instance}')
            logger.info(f'Updated Author with name : {serializer.instance}')
            return Response (serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})

    def delete(self,request, id):
        author = self.get_object(id)
        author.delete()
        logger.debug(f'Deleted Author with name: {author.first_name}')
        logger.info(f'Deleted Author with name : {author.first_name}')
        return Response({'Author deleted': True})

    permission_classes = (IsAuthenticated,)


class AuthorListAPIView(APIView):
    def get(self,request):
        author = Author.objects.all()
        # author = AuthorManager.all()
        serializer = AuthorModelSerializer(author, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = AuthorModelSerializer(data=request.data)
        # instance.emails_for_help.add(*users)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Created Author with name: {serializer.instance}')
            logger.info(f'Created Author with name : {serializer.instance}')
            return Response (serializer.data , status=status.HTTP_201_CREATED)


        return Response ({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuthorDetailAPIView(APIView):
    def get_object(self , id):
        try:
            return Author.objects.get(id = id)
        except Author.DoesNotExist as e:
            return Response({'Error':str(e)})

    def get(self, request , id):
        author = self.get_object(id)
        serializer = AuthorModelSerializer(author)
        return Response(serializer.data)

    def put(self, request , id):
        author = self.get_object(id)
        serializer = AuthorModelSerializer(instance=author , data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Updated Author with name: {serializer.instance}')
            logger.info(f'Updated Author with name : {serializer.instance}')
            return Response (serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})

    def delete(self,request, id):
        author = self.get_object(id)
        author.delete()
        logger.debug(f'Deleted Author with name: {author.first_name}')
        logger.info(f'Deleted Author with name : {author.first_name}')
        return Response({'Author deleted': True})

    permission_classes = (IsAuthenticated,)

class BookCategoryListAPIView(APIView):
    def get(self,request):
        book_category = BookCategory.objects.all()
        serializer = BookCategorySerializer(book_category, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = BookCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Created Book Category with name: {serializer.instance}')
            logger.info(f'Created Book Category with name : {serializer.instance}')
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response ({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookCategoryDetailAPIView(APIView):
    def get_object(self , id):
        try:
            return BookCategory.objects.get(id = id)
        except BookCategory.DoesNotExist as e:
            return Response({'Error':str(e)})

    def get(self, request , id):
        book_category = self.get_object(id)
        serializer = BookCategorySerializer(book_category)
        return Response(serializer.data)

    def put(self, request , id):
        book_category = self.get_object(id)
        serializer = BookCategorySerializer(instance=book_category , data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Updated book_category with name: {serializer.instance}')
            logger.info(f'Updated book_category with name : {serializer.instance}')
            return Response (serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})

    def delete(self,request, id):
        book_category = self.get_object(id)
        book_category.delete()
        logger.debug(f'Deleted Author with name: {book_category.name}')
        logger.info(f'Deleted Author with name : {book_category.name}')
        return Response({'book_category deleted': True})

    # permission_classes = (IsAuthenticated,)