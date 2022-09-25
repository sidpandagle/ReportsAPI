from typing import Optional
from fastapi import FastAPI, Depends, status, HTTPException
from models import Base, Category 
from schemas import ICategory, ICategoryUpdate
from database import engine, SessionLocal
from sqlalchemy.orm import Session

import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# Base API Call
@app.get('/')
def hello():
    return {"message": "API Running"}

# Add Category
@app.post('/category', status_code=status.HTTP_201_CREATED)
def add_category(category: ICategory, db: Session = Depends(get_db)):
    new_Category = Category(title=category.title)
    db.add(new_Category)
    db.commit()
    db.refresh(new_Category)
    return new_Category

# Get Category
@app.get('/category')
def get_category(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories

# Get Category By Id
@app.get('/category/{id}')
def get_category_by_id(id:int,db: Session = Depends(get_db)):
    category = db.query(Category).get(id)
    return category

# Update Category
@app.put('/category')
def update_category(newCategory: ICategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(Category).get(newCategory.id)
    
    if category:
        category.title = newCategory.title
        db.commit()
        db.refresh(category)

    if not category:
        raise HTTPException(status_code=404, detail=f"Category with id {id} not found")

    return category

# Delete Category
@app.delete('/category/{id}')
def delete_category(id:int,db: Session = Depends(get_db)):
    category = db.query(Category).get(id)

    if category:
        db.delete(category)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Category with id {id} not found")

    return "Category Deleted"



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
