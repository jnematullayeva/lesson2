from fastapi import FastAPI
import book.models
# import account.models
from database import engine

app = FastAPI()

book.models.Base.metadata.create_all(bind=engine)
# account.models.Base.metadata.create_all(bind=engine)

@app.get("/")
def test():
    return {"Message": "Main page"}
