from fastapi import status
from fastapi.exceptions import HTTPException
from models import Product
from schema import ProductCreate
from sqlalchemy.orm import Session

def product_create(db: Session, product: ProductCreate):

    new_product = Product(
        name=product.name,
        price=product.price,
        description=product.description
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def product_list(db: Session):
   products = db.query(Product).all()
   return products

