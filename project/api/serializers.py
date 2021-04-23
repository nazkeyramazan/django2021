from rest_framework import serializers
from api.models import *

#serializers.Serializer
class MainCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        main_category = MainCategory.objects.create(name=validated_data.get('name'))
        return main_category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
class BookCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    def create(self, validated_data):
        book_category = BookCategory.objects.create(name=validated_data.get('name') , description=validated_data.get('description'))
        return book_category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

#model Serializer
class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name' , 'address', 'city' , 'country')
class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name' , 'last_name', 'email')

#Nested
class BookSerializer(serializers.ModelSerializer):
    category = BookCategorySerializer(read_only= True)
    publisher = PublisherModelSerializer(read_only=True)
    author = AuthorModelSerializer( many=True)
    class Meta:
        model = Book
        fields = ('name', 'description' , 'price', 'category' ,'publisher' , 'author' )
    def create(self, validated_data):
        author_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        for track_data in author_data:
            Author.objects.create(book=book, **track_data)
        return book

#inheritance Serializer
class BookDetailSerializer(BookSerializer):
    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields +  ('genre' , 'num_pages')
