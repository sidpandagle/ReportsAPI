from fastapi import Depends, status, HTTPException, APIRouter
from models import  Report as ReportModel 
from schemas import report as ReportSchema
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/report")

# Add Report
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_report(report: ReportSchema.IReport, db: Session = Depends(get_db)):
    new_Report = ReportModel(
        title=report.title,
        category_id=report.category_id,
        price=report.price,
        description=report.description,
        )
    db.add(new_Report)
    db.commit()
    db.refresh(new_Report)
    return new_Report

# Get Report
@router.get('/')
def get_report(db: Session = Depends(get_db)):
    reports = db.query(ReportModel).all()
    return reports

# Get Report By Id
@router.get('/{id}')
def get_report_by_id(id:int,db: Session = Depends(get_db)):
    report = db.query(ReportModel).get(id)
    return report

# Update Report
@router.put('/')
def update_report(newReport: ReportSchema.IReportUpdate, db: Session = Depends(get_db)):
    report = db.query(ReportModel).get(newReport.id)
    
    if report:
        report.title = newReport.title
        report.price = newReport.price
        report.category_id = newReport.category_id
        report.description = newReport.description
        db.commit()
        db.refresh(report)

    if not report:
        raise HTTPException(status_code=404, detail=f"Report with id {id} not found")

    return report

# Delete Report
@router.delete('/{id}')
def delete_report(id:int,db: Session = Depends(get_db)):
    report = db.query(ReportModel).get(id)

    if report:
        db.delete(report)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Report with id {id} not found")

    return "Report Deleted"