from fastapi import FastAPI

app = FastAPI()

@app.get('/get_patients')
async def get_patients():
    return {'message':'Liste des patients'}

@app.post('/add_patient')

async def add_patient():
    return {'message':'Ajouter patients'}
