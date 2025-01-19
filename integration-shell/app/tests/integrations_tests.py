# pytest app/tests/
# pytest app/tests/
# pytest app/tests/
# pip install pytest httpx
# pip install pytest httpx
# pip install pytest httpx


from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_integration():
    response = client.post("/integrations/", json={
        "name": "Slack",
        "description": "Integración con Slack"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Slack"



def test_list_integrations():
    response = client.get("/integrations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
