from fastapi import Depends, status, HTTPException, APIRouter
from models import  ReportSample as ReportSampleModel 
from schemas import reportsample as  ReportSampleSchema
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/reportsample")

# Add ReportSample
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_report_sample(reportsample: ReportSampleSchema.IReportSample, db: Session = Depends(get_db)):
    new_ReportSample = ReportSampleModel(
        name=reportsample.name,
        email=reportsample.email,
        country=reportsample.country,
        phone=reportsample.phone,
        company_name=reportsample.company_name,
        )
    db.add(new_ReportSample)
    db.commit()
    db.refresh(new_ReportSample)
    return new_ReportSample

# Get ReportSample
@router.get('/')
def get_report_sample(db: Session = Depends(get_db)):
    rs = db.query(ReportSampleModel).all()
    return rs

# Get ReportSample By Id
@router.get('/{id}')
def get_report_sample_by_id(id:int,db: Session = Depends(get_db)):
    rs = db.query(ReportSampleModel).get(id)
    return rs