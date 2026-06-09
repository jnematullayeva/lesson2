from pydantic import BaseModel, Field
from typing import Optional

class BookCreateSchema(BaseModel):
    title: str
    desc: str



class BookOutSchema(BaseModel):
    id: int

class BookCreateSchema(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None
