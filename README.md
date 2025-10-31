# AI Cardio RISK Prediction

## 📁 Structure du projet

    project/
    │
    ├── ml/ # Partie Machine Learning
    │ ├── eda.ipynb
    │ ├── data.csv
    │ ├── model_xgboost.pkl
    │ └── model_cardio.pkl
    │
    ├── Backend_Fast_API/ 
    │ ├── main.py 
    │ ├── Database.py 
    │ ├── models.py 
    │ ├── patient.py
    | ├── patients.db
    │ └── test_status_code.py
    │
    ├── .gitignore 
    ├── README.md
    └── requirements.txt

## Partie Backend (FastAPI)

- API développée avec FastAPI.

- Base de données : SQLite via SQLAlchemy.

- Documentation automatique disponible sur :

    - Swagger UI → http://127.0.0.1:8000/docs

### Lancer le serveur
    uvicorn backend.main:app --reload
### Exécuter les tests
    pytest Backend_Fast_API/test_status_code.py/

### Technologies utilisées
- Python

- FastAPI

- SQLAlchemy

- SQLite

- Pydantic

- Swagger

- pytest / TestClient


# Auteurs
- **Karima Ben Ihda**
- **Saida Aourras**



