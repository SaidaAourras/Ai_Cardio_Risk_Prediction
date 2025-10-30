from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from . import models,schemas,crud
from .database import engine,SessionLocal
import joblib
import numpy as np

models.Base.metadata.create_all(bind=engine)
app=FastAPI()

model=joblib.load("app/model_cardio.pkl")

def get_db():
    db=SessionLocal()
    try:
        yield db
    
    finally:
        db.close()
        
@app.get("/patients",response_model=list[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_patients(db,skip,limit)

@app.post("/patients/create_patient",response_model=schemas.Patient)
def create_patient(patient:schemas.PatientCreate,db:Session=Depends(get_db)):
    return crud.create_patient(db=db,patient=patient)

