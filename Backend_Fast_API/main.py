from fastapi import FastAPI , Depends
from Database import  PatientCreate , get_db
from patient import Patient 
from sqlalchemy.orm import Session
import pandas as pd
from fastapi import HTTPException
import json
import joblib

app = FastAPI()


# lister les patients
@app.get('/patients/get_patients/')
async def get_patients(skip:int=0 , limit=10 ,db:Session= Depends(get_db)):
    patients = db.query(Patient).offset(skip).limit(limit).all()
    return patients


#  renvoi objet de type query pas list liste des patients
# apres l'ajout de .all(), .first(), .limit(), etc => SQLAlchemy exécute vraiment la requête
# resulat : <sqlalchemy.orm.query.Query object at 0x...>
# FastAPI ne peux pas convertir en json => donc rien ne s’affiche.


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
    model = joblib.load('../ml/model_cardio.pkl')
    patient = db.query(Patient).first()

    features_model = ['age','gender', 'pressurehight','pressurelow',  'glucose', 'kcm','troponin',  'impluse']
    
    
    # chaque objet python contient des fonction __dict__
    # renvoie dictionnaire contenant tous les attributs de l’objet patient et leurs valeurs
    # .items() renvoie la liste des paires (clé, valeur) du dictionnaire
      
    dict_patient = patient.__dict__
    pd_patient = pd.DataFrame([dict_patient]).drop(columns=['status','id'], errors='ignore')
    pd_patient = pd_patient.reindex(columns=features_model)
    status = model.predict(pd_patient)
    
    # try:
    #     status = model.predict(pd_patient)
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Erreur pendant la prédiction : {e} \n {pd_patient.to_string()}")

    return {'status': int(status[0])}
    



