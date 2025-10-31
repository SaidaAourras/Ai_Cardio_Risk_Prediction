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

# API de machine learning (Santé)

### Créer une API complète d’aide à la décision médicale capable de prédire le risque de maladie cardiovasculaire à partir des données d’un patient.

# Partie Machine Learning
## -charger et afficher les données : read_csv 

## -Vérifier la redondance , les valeurs null et les champs vides: describe,duplicated,isnull

## matrice de corrélation

## Visulation des variables categoriels:countplot du repartition des status selon l'age

## Split et Normalisation des donnees: StandardScaler

## Entrainement du model:RandomForestClassifier && XGBClassifier

## Saver le model avec joblib



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



