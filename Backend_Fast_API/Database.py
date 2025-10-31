from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , declarative_base
from pydantic import BaseModel


DATABASE_URL = 'sqlite:///./patients.db'

# moteur SQLAlchemy lié à cette base
engine = create_engine(DATABASE_URL)

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
    
    

        


