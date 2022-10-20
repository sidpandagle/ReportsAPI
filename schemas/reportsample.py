from pydantic import BaseModel

class IReportSample(BaseModel):
    id: int
    name: str
    email: str
    country: str
    phone: str
    company_name: str
