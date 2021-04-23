from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from api.models import MainCategory , BookCategory
from api.serializers import MainCategorySerializer ,BookCategorySerializer

@api_view(['GET', 'POST'])
def main_category_list(request):
    if request.method == 'GET':
        main_categories = MainCategory.objects.all()
        serializer = MainCategorySerializer(main_categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MainCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error :(': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def main_category_detail(request, main_category_id):
    try:
        main_category = MainCategory.objects.get(id=main_category_id)
    except MainCategory.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = MainCategorySerializer(main_category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MainCategorySerializer(instance=main_category, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        main_category.delete()
        return Response({'Main category item deleted': True})

@api_view(['GET', 'POST'])
def book_category_list(request):
    if request.method == 'GET':
        book_categories = BookCategory.objects.all()
        serializer = BookCategorySerializer(book_categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error :(': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def book_category_detail(request, book_category_id):
    try:
        book_category = BookCategory.objects.get(id=book_category_id)
    except BookCategory.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = BookCategorySerializer(book_category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookCategorySerializer(instance=book_category, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        book_category.delete()
        return Response({'Book category deleted': True})
