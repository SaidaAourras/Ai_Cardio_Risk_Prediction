from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from pydantic import BaseModel
# import pandas as pd


# df = pd.read_csv('../patients.csv')

DATABASE_URL = 'sqlite:///./patients.db'


# moteur SQLAlchemy lié à cette base
engine = create_engine(DATABASE_URL ,connect_args={"check_same_thread":False})
# df.to_sql('patients', con=engine , index=False , if_exists='replace')

# session locale pour gerer les transactions
SessionLocal = sessionmaker(autocommit=False ,autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

class PatientCreate(BaseModel):
    age : int
    gender : int
    status : str
    pressurehight  : int
    pressurelow : int
    glucose : int
    kcm : float
    troponin : float
    impluse : int
    
    
# A revoir 
  
# class PatientResponse(PatientCreate):
    # id: int

    # class Config:
    #     orm_mode = True
        


