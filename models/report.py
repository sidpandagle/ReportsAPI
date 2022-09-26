from sqlalchemy import Column, Integer, String
from database import Base

class Report(Base):
    __tablename__ = 'Report'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category_id = Column(Integer)
    price = Column(Integer)
    description = Column(String)
