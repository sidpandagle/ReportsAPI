from pydantic import BaseModel

class ICategory(BaseModel):
    title: str

class ICategoryUpdate(BaseModel):
    id: int
    title: str
