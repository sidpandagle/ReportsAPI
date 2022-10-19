from sqlalchemy import Column, Integer, String
from database import Base

class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60))


class Report(Base):
    __tablename__ = 'Report'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60))
    # category = Column(String(60))
    # price = Column(Integer)
    description = Column(String())
