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
class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()

    def create(self, validated_data):
        publisher = Publisher.objects.create(name=validated_data.get('name'),
                                             address=validated_data.get('address'),
                                             city=validated_data.get('city'),
                                             country=validated_data.get('country'),
                                             )
        return publisher

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance

    def validate(self, data):
        if data['name'] == '':
            raise serializers.ValidationError("Enter Publisher name")
        return data

#model Serializer
class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name' , 'address', 'city' , 'country')

class BookCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory

        fields = ('id', 'name', 'description')


class BookSerializer(serializers.ModelSerializer):
    # category = BookCategorySerializer(read_only= True)
    # publisher = PublisherModelSerializer(read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

        # fields = ('name', 'description' , 'price','category' ,'publisher' ,'author' )
        # extra_kwargs = {'author': {'required': False}}
    #
    # def create(self, validated_data):
    #     author_data = validated_data.pop('author')
    #     book = Book.objects.create(**validated_data)
    #     for track_data in author_data:
    #         Author.objects.create(book=book, **track_data)
    #     return book
class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        books = BookSerializer(many=True, read_only=True)
        fields = ('id', 'first_name' , 'last_name', 'email' , 'books')
        # extra_kwargs = {'books': {'required': False}}

#inheritance Serializer
class BookDetailSerializer(BookSerializer):
    class Meta(BookSerializer.Meta):
        # fields = BookSerializer.Meta.fields +  ('genre' , 'num_pages')
        fields = '__all__'
