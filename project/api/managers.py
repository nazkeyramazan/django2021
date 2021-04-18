from django.db import models

class BookManager(models.Manager):

    def get_by_author_with_relation(self, author_id):
        return self.get_related().filter(author_id=author_id)

    def get_by_author_without_relation(self, author_id):
        return self.filter(author_id=author_id)

    def get_related(self):
        return self.select_related('author', 'publisher')

class PublisherManager(models.Manager):

    def get_publicher_from_kz(self):
        return self.filter(coutry = "Kazakhstan")

    def get_publicher_from_kz_ru_uk(self):
        return self.filter(coutry = ["Kazakhstan" ,"Russia" , "Ukraine"])

class BookDetailManager(BookManager):

    def get_genre_educational(self):
        return self.filter(genre = "Educational")

    def get_genre_classic(self):
        return self.filter(genre = "Classic")
