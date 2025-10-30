from sqlalchemy.orm import Session
from . import models,schemas

def get_patients(db:Session,skip:int=0,limit:int=10):
    return db.query(models.Patient).offset(skip).limit(limit).all()


def create_patient(db:Session,patient:schemas.PatientCreate):
    db_patient=models.Patient(
    age=patient.age,
    gender=patient.gender,
    status=patient.status,
    pressurehight=patient.pressurehight,
    pressurelow=patient.pressurelow,
    glucose=patient.glucose,
    kcm=patient.kcm,
    troponin=patient.troponin,
    impluse=patient.impluse)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

