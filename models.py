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

class ReportSample(Base):
    __tablename__ = 'ReportSample'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60))
    email = Column(String(50))
    country = Column(String(30))
    phone = Column(String(20))
    company_name = Column(String(60))
