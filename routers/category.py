from fastapi import Depends, status, HTTPException, APIRouter
from models.category import  Category as CategoryModel 
from schemas import category as  CategorySchema
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/category")

# Add Category
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_category(category: CategorySchema.ICategory, db: Session = Depends(get_db)):
    new_Category = CategoryModel(title=category.title)
    db.add(new_Category)
    db.commit()
    db.refresh(new_Category)
    return new_Category

# Get Category
@router.get('/')
def get_category(db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).all()
    return categories

# Get Category By Id
@router.get('/{id}')
def get_category_by_id(id:int,db: Session = Depends(get_db)):
    category = db.query(CategoryModel).get(id)
    return category

# Update Category
@router.put('/')
def update_category(newCategory: CategorySchema.ICategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).get(newCategory.id)
    
    if category:
        category.title = newCategory.title
        db.commit()
        db.refresh(category)

    if not category:
        raise HTTPException(status_code=404, detail=f"Category with id {id} not found")

    return category

# Delete Category
@router.delete('/{id}')
def delete_category(id:int,db: Session = Depends(get_db)):
    category = db.query(CategoryModel).get(id)

    if category:
        db.delete(category)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Category with id {id} not found")

    return "Category Deleted"