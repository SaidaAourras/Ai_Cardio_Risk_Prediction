from pydantic import BaseModel

class PatientBase(BaseModel):
    age:int
    gender:int
    status:str
    pressurehight:int
    pressurelow:int
    glucose:int
    kcm:float
    troponin:float
    impluse:int


class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id:int
    
    class Config:
        from_attributes =True

