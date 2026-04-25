from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_list_demo_companies() -> None:
    response = client.get("/api/v1/demo/companies")

    assert response.status_code == 200
    assert response.json()[0]["source"] == "demo"


def test_demo_risk_score() -> None:
    response = client.get("/api/v1/demo/companies/1/risk")

    assert response.status_code == 200
    assert response.json()["risk_level"] == "medium"


def test_create_and_get_demo_privacy_request() -> None:
    create_response = client.post("/api/v1/demo/companies/1/privacy-requests")

    assert create_response.status_code == 201
    request_id = create_response.json()["id"]

    status_response = client.get(f"/api/v1/demo/privacy-requests/{request_id}")

    assert status_response.status_code == 200
    assert status_response.json()["status"] == "draft"
