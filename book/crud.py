from fastapi  import status
from fastapi.exceptions import HTTPException
from models import Book
from schema import BookCreate
from sqlalchemy.orm import Session

def book_create(db: Session, book: BookCreate):
    new_book = Book(
        title=book.title,
        desc=book.desc
    )
    db.add(new_book)  #new_bookni dbga qo'shish ... new_book.save()
    db.commit()
    db.refresh(new_book)
    return new_book

def book_list(db: Session):
   books = db.query(Book).all() #Books.objects.
   return books

