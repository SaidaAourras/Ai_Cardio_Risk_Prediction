import joblib
import pandas as pd
# import numpy as np

model = joblib.load('../ml/model_cardio.pkl')

data = pd.read_csv('../ml/data.csv').drop(columns=['status'])
# print(data)

for d in data.to_dict(orient='records'):
    
    predict = pd.DataFrame([d])

    prediction = model.predict(predict)
    # print(type(prediction))
    print("Sortie du modèle :", prediction)
