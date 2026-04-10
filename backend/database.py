"""
Database Module
Handles database operations for storing and retrieving medical reports
"""

import os
from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Date, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dotenv import load_dotenv

load_dotenv()

# Database URL configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///medical_reports.db')

# Create database engine
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Patient(Base):
    """Database model for patients"""
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(20), nullable=False)
    medical_record_number = Column(String(50), unique=True, nullable=False)
    phone = Column(String(30))
    email = Column(String(255))
    address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    reports = relationship('MedicalReport', back_populates='patient')


class MedicalReport(Base):
    """Database model for medical reports"""
    __tablename__ = 'medical_reports'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=True)
    filename = Column(String(255), unique=True, index=True)
    original_text = Column(Text)
    ai_analysis = Column(Text)
    provider = Column(String(50), default='openai')
    model = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    patient = relationship('Patient', back_populates='reports')


def init_db():
    """Initialize database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully")
        return True
    except Exception as e:
        print(f"Error initializing database: {e}")
        return False


def create_patient(patient_name, date_of_birth, gender, phone='', email='', address=''):
    """Create a new patient record in the database. MRN is auto-generated after insert."""
    try:
        session = SessionLocal()
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d').date() if isinstance(date_of_birth, str) else date_of_birth
        patient = Patient(
            patient_name=patient_name,
            date_of_birth=dob,
            gender=gender,
            medical_record_number='PENDING',  # temporary; replaced after we have patient_id
            phone=phone or '',
            email=email or '',
            address=address or '',
        )
        session.add(patient)
        session.commit()
        session.refresh(patient)
        # Now we have the auto-incremented patient_id — generate the real MRN
        from datetime import date as _date
        year = _date.today().year
        mrn = f'MRN-{year}-{patient.patient_id:04d}'
        patient.medical_record_number = mrn
        session.commit()
        pid = patient.patient_id
        session.close()
        return {'status': 'success', 'patient_id': pid, 'medical_record_number': mrn}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}


def store_report(filename, original_text, ai_analysis, patient_id=None, provider='openai', model='gpt-4'):
    """
    Store medical report in database

    Args:
        filename (str): Original filename
        original_text (str): Extracted text from PDF
        ai_analysis (str): AI processing results
        patient_id (int): Associated patient ID (optional)
        provider (str): LLM provider used
        model (str): Model name used

    Returns:
        dict: Storage result
    """
    try:
        session = SessionLocal()
        report = MedicalReport(
            filename=filename,
            original_text=original_text,
            ai_analysis=ai_analysis,
            patient_id=patient_id,
            provider=provider,
            model=model
        )
        session.add(report)
        session.commit()
        report_id = report.id
        session.close()
        
        return {
            'status': 'success',
            'report_id': report_id,
            'message': 'Report stored successfully'
        }
    except Exception as e:
        return {
            'status': 'failed',
            'error': str(e)
        }


def get_report(report_id):
    """
    Retrieve report by ID
    
    Args:
        report_id (int): Report ID
        
    Returns:
        dict: Report data or error
    """
    try:
        session = SessionLocal()
        report = session.query(MedicalReport).filter(MedicalReport.id == report_id).first()
        session.close()
        
        if report:
            return {
                'status': 'success',
                'report': {
                    'id': report.id,
                    'patient_id': report.patient_id,
                    'filename': report.filename,
                    'original_text': report.original_text,
                    'ai_analysis': report.ai_analysis,
                    'provider': report.provider,
                    'model': report.model,
                    'created_at': str(report.created_at),
                    'updated_at': str(report.updated_at)
                }
            }
        else:
            return {
                'status': 'failed',
                'error': 'Report not found'
            }
    except Exception as e:
        return {
            'status': 'failed',
            'error': str(e)
        }


def get_all_reports():
    """
    Retrieve all reports
    
    Returns:
        list: All reports
    """
    try:
        session = SessionLocal()
        reports = session.query(MedicalReport).all()
        session.close()
        
        return {
            'status': 'success',
            'reports': [
                {
                    'id': r.id,
                    'patient_id': r.patient_id,
                    'filename': r.filename,
                    'provider': r.provider,
                    'model': r.model,
                    'created_at': str(r.created_at),
                    'updated_at': str(r.updated_at)
                }
                for r in reports
            ],
            'count': len(reports)
        }
    except Exception as e:
        return {
            'status': 'failed',
            'error': str(e)
        }


def delete_report(report_id):
    """
    Delete report by ID
    
    Args:
        report_id (int): Report ID
        
    Returns:
        dict: Deletion result
    """
    try:
        session = SessionLocal()
        report = session.query(MedicalReport).filter(MedicalReport.id == report_id).first()
        
        if report:
            session.delete(report)
            session.commit()
            session.close()
            return {
                'status': 'success',
                'message': 'Report deleted successfully'
            }
        else:
            session.close()
            return {
                'status': 'failed',
                'error': 'Report not found'
            }
    except Exception as e:
        return {
            'status': 'failed',
            'error': str(e)
        }
