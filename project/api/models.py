from django.db import models
from api.managers import BookManager , PublisherManager , BookDetailManager , AuthorManager
# Main category which will appear in main page of the site
# Book
#Technologies
#Sport
#etc
class MainCategory(models.Model):
    name = models.CharField(verbose_name='Category name' , max_length=255 , unique=True , default="Maincc")
    # description = models.TextField(verbose_name="Category description" , default="No description, add description" )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Main category"
        # verbose_name_plural="Main categories"

class BookCategory(models.Model):
    name = models.CharField(verbose_name='Book category name' , max_length=255 , unique=True ,  default="some")
    description = models.TextField(verbose_name="Book category description" , default="No description, add description" )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Book category"
        verbose_name_plural="Book categories"

class Publisher(models.Model):
    name = models.CharField(max_length=255 , verbose_name="Publisher name"),
    address = models.CharField(max_length=255 , verbose_name="Publisher address"),
    city = models.CharField(max_length=255 , verbose_name="Publisher city")
    country = models.CharField(max_length=255 , verbose_name="Publisher country")
    object  = PublisherManager()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Publisher"
        verbose_name_plural="Publishers"

class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Name')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Surname')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')
    object = AuthorManager()
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Book(models.Model):
    name = models.CharField(max_length=1000,  verbose_name="Book name"  )
    description = models.TextField(max_length=10000,default="No data" ,verbose_name='Book description')
    price = models.IntegerField( default='No data' , verbose_name='Book price')
    category = models.ForeignKey(BookCategory ,on_delete=models.CASCADE , verbose_name="Category")
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, null=True, blank=True, verbose_name='Publsiher')
    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.name

    object = BookManager()

    class Meta:
        verbose_name="Book"
        verbose_name_plural="Books"

class BookDetail(Book):
    genre = models.CharField(max_length=255, verbose_name="Book genre"),
    num_pages = models.IntegerField()

    object = BookDetailManager()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Book detail"
        verbose_name_plural="Books details"