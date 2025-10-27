from fastapi import FastAPI

app = FastAPI()

@app.get('/')

async def root():
    return {'message':'hello world'}

@app.post('/')

async def post():
    return {'message':'hello post'}

@app.put('/', description='hello')
async def put():
    return {'message':'put'}