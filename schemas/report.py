from pydantic import BaseModel

class IReport(BaseModel):
    title: str
    category_id: int
    price: int
    description: str

class IReportUpdate(BaseModel):
    id: int
    title: str
    category_id: int
    price: int
    description: str