from urllib import response
from fastapi  import Depends, status
from fastapi.exceptions import HTTPException
from book.models import Book
from book.schema import BookCreateSchema, BookCreateschema, BookOutSchema
from sqlalchemy.orm import Session

from database import get_db
from supermarket import router

def book_create(db: Session, book: BookCreateschema):
    new_book = Book(
        title=book.title,
        desc=book.desc
    )
    db.add(new_book)  #new_bookni dbga qo'shish ... new_book.save()
    db.commit()
    db.refresh(new_book)
    
    response = {
        'msg': "Book created",
        'status': status.HTTP_201_CREATED,
        'id': new_book.id
    }
    return response

def book_list(db: Session):
   books = db.query(Book).all() #Books.objects.
   response = {
        'msg': "Books",
        'status': status.HTTP_200_OK,
        'count': len(books),
        'book': books
   }
   return response

def book_detail(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    response = {
        'msg': "Book details",
        'status': status.HTTP_200_OK,
        'book': book
    }
    return response


@router.get('/detail/{book_id}')
def book_detail_router(book_id: int, db: Session = Depends(get_db)):
    return book_detail(db, book_id)

def book_delete(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    db.delete(book)
    db.commit()

    response = {
        'msg': "Book deleted",
        'status': status.HTTP_204_NO_CONTENT
    }
    return response

@router.delete('/delete/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def book_delete_router(book_id: int, db: Session = Depends(get_db)):
    return book_delete(db, book_id)


def book_update(db: Session, book_id: int, book_data: BookCreateSchema):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    # if book_data.title:
    #     book.title = book_data.title

    # if book_data.desc:
    #     book.desc = book_data.desc


    for key, value in book_data.dict().items():
            if value is not None:
                setattr(book, key, value)            
    db.commit()
    db.refresh(book)

    response = {
        'msg': "Book updated",  
        'status': status.HTTP_200_OK,
        'book': book
    }
    return response