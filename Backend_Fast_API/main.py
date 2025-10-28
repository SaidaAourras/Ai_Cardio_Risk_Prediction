from fastapi import FastAPI , Depends
from Database import  PatientCreate , get_db
from patient import Patient 
from sqlalchemy.orm import Session

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



