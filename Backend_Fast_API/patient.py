import Database as db
from sqlalchemy import Column , Integer , String , Float



Base = db.Base
engine = db.engine
SessionLocal = db.SessionLocal


class Patient(Base):
    __tablename__ ='patients'
    
    id = Column(Integer , primary_key=True , index= True)
    age = Column(Integer , index= True)
    gender = Column(Integer)
    status = Column(String)
    pressurehight  = Column(Integer)
    pressurelow = Column(Integer)
    glucose = Column(Integer)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Integer)
    
Base.metadata.create_all(bind=engine)

    
    
    





    


    