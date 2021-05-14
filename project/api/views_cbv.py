from rest_framework.decorators import APIView
from rest_framework import  status
from rest_framework.response import Response
from api.serializers import *
from api.models import *
from api.managers import BookManager , PublisherManager , BookDetailManager , AuthorManager

from rest_framework.permissions import IsAdminUser,IsAuthenticated

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
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response ({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuthorDetailAPIView(APIView):
    def get_object(self , id):
        try:
            return Author.objects.get(id = id)
        except Author.DoesNotExist as e:
            return Response({'Error':str(e)})

    def get(self, request , shedule_id):
        author = self.get_object(shedule_id)
        serializer = AuthorModelSerializer(author)
        return Response(serializer.data)

    def put(self, request , id):
        author = self.get_object(id)
        serializer = AuthorModelSerializer(instance=author , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})

    def delete(self,request, id):
        author = self.get_object(id)
        author.delete()
        return Response({'deleted': True})

    # permission_classes = (IsAuthenticated,IsAdminUser,)