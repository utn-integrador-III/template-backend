from db.book_db_connection import BookDBConnection
from decouple import config
from utils.commons import Commons
import pandas
connection = BookDBConnection(config("BOOKS_COLLECTION"))


class Book:
    id =" ",
    name = " ",
    author=" ",
    gender=" "

    def __init__(
            self,
            id,
            name,
            author,
            gender
    ):
        self.id = id,
        self.name = name,
        self.author = author,
        self.gender = gender


    @classmethod
    def get_by_name(self, name):
        list_books = {}
        return list(list_books.to_dict(orient='records'))
    
    @classmethod
    def get_book_by_key(self, book_key):
        list_books = {}
        return list_books


        