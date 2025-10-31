from fastapi import FastAPI , Depends
from Database import  PatientCreate , get_db
from patient import Patient 
from sqlalchemy.orm import Session
import pandas as pd
import joblib

app = FastAPI()


# lister les patients
@app.get('/patients/get_patients/')
async def get_patients(db:Session= Depends(get_db)):
    patients = db.query(Patient).all()
    return patients


# ajouter patient
@app.post('/patients/add_patient/')
async def create_patient(patient:PatientCreate , db:Session = Depends(get_db)):
    db_patient = Patient(
        age = patient.age,
        gender = patient.gender,
        status = patient.status,
        pressurehight  = patient.pressurehight,
        pressurelow = patient.pressurelow,
        glucose =patient.glucose ,
        kcm = patient.kcm ,
        troponin = patient.troponin ,
        impluse = patient.impluse
    )
    
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


@app.get('/patients/predict_risk')
async def predict_risk(db:Session = Depends(get_db)):
    
    model = joblib.load('../ml/model_random_forest_cardio.pkl')
    patient = db.query(Patient).order_by(Patient.id.desc()).first()
    features_model = ['age','gender', 'pressurehight','pressurelow',  'glucose', 'kcm','troponin',  'impluse']
    
    dict_patient = patient.__dict__
    pd_patient = pd.DataFrame([dict_patient]).drop(columns=['status','id'], errors='ignore')
    pd_patient = pd_patient.reindex(columns=features_model)
    status = model.predict(pd_patient)
    
    return {'status': int(status[0])}
    



