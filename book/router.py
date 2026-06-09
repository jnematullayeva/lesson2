from fastapi import APIRouter, Depends
from book import crud
from schema import BookCreate, BookOut
from sqlalchemy.orm import Session
from main import get_db
from book.crud import book_create, book_list, book_update, book_delete
from fastapi import status
from typing import List

router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=BookOut)
def book_create_router(book: BookCreate, db: Session = Depends(get_db)):
    return book_create(db, book)


@router.get('/list', response_model=list[BookOut])
def Book_list_router(db: Session = Depends(get_db)):
    return book_list(db)


@router.get('/detail/{book_id}', response_model=BookOut)
def book_detail_router(book_id: int, db: Session = Depends(get_db)):
    return crud.book_detail(db, book_id)    

@router.delete('/delete/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def book_delete_router(book_id: int, db: Session = Depends(get_db)):
    return crud.book_delete(db, book_id)

@router.patch('/update/{book_id}', response_model=BookOut)
def book_update_router(book_id: int, book_data: BookCreate, db: Session =   Depends(get_db)):
    return book_update(db, book_id, book_data)