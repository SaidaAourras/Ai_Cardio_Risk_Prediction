from fastapi.testclient import TestClient
from main import app

cleint = TestClient(app)
def test_status_code():
    response = cleint.get('/patients/predict_risk')
    # print(response.status_code)
    assert response.status_code == 200