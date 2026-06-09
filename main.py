from fastapi import FastAPI
from database import SessionLocal
from book.router import router as book_router

app = FastAPI()

app.include_router(book_router, prefix="/book")

@book_router.get("/")
def index():
    return {"message": "Main"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()