from api.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.serializers import PublisherModelSerializer
from api.models import Publisher
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
# class PublisherViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Publisher.objects.all()
#         serializer = PublisherModelSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self , request):
#         serializer = PublisherModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'Error :(': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     def retrieve(self, request, id):
#         queryset = Publisher.objects.all()
#         publisher = get_object_or_404(queryset, id=id)
#         serializer = PublisherModelSerializer(publisher)
#         return Response(serializer.data)