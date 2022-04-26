class BookCard:
    author: str
    title: str
    year: int

    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def __repr__(self):
        return repr((self.author, self.title, self.year))


book_objects = [
    BookCard('author1', 'title1', 1999),
    BookCard('author2', 'title2', 2001),
    BookCard('author3', 'title3', 2015),
]

print(sorted(book_objects, key=lambda book: book.year))

# @property
# def author(self):
#     return self.__author
#
# @author.setter
# def author(self, value):
#     if isinstance(value, str):
#         self.__author = value
#     else:
#         raise ValueError
#
# @property
# def title(self):
#     return self.__title
#
# @title.setter
# def title(self, value):
#     if isinstance(value, str):
#         self.title = value
#     else:
#         raise ValueError
#
# @property
# def year(self):
#     return self.__year
#
# @year.setter
# def year(self, value):
#     if isinstance(value, int):
#         self.year = value
#     else:
#         raise ValueError
