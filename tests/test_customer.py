from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def teardown():
    # Code to run before each test
    yield
    # Code to run after each test
    # Fetch all customers
    response = client.get("/customers/")
    customers = response.json()

    # Delete each customer
    for customer in customers:
        customer_id = customer["id"]
        client.delete(f"/customers/{customer_id}")


def test_create_customer():
    response = client.post(
        "/customers/", json={"name": "John Doe", "address_city": "New York"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


def test_read_all_customers():
    # First, create a few customers
    client.post("/customers/",
                json={"name": "Alice Doe",
                      "address_city": "Boston"})
    client.post("/customers/",
                json={"name": "Bob Doe",
                      "address_city": "Seattle"})

    # Now, test the 'read all customers' endpoint
    response = client.get("/customers/")

    # Assert the status code is OK
    assert response.status_code == 200

    # Assert the response contains a list of customers and
    # that at least the two created are in the list
    customers = response.json()
    assert len(customers) >= 2  # Ensure that at least two customers exist
    assert any(customer["name"] == "Alice Doe" for customer in customers)
    assert any(customer["name"] == "Bob Doe" for customer in customers)


def test_read_customer():
    response = client.post(
        "/customers/", json={"name": "Jane Doe", "address_city": "Los Angeles"}
    )
    customer_id = response.json()["id"]
    response = client.get(f"/customers/{customer_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"


def test_update_customer():
    response = client.post(
        "/customers/", json={"name": "Jack Doe", "address_city": "Chicago"}
    )
    customer_id = response.json()["id"]
    response = client.put(
        f"/customers/{customer_id}",
        json={"name": "Jack Smith", "address_city": "Chicago"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Jack Smith"


def test_delete_customer():
    response = client.post(
        "/customers/",
        json={"name": "Emily Doe", "address_city": "San Francisco"},
    )
    customer_id = response.json()["id"]
    response = client.delete(f"/customers/{customer_id}")
    assert response.status_code == 200
    response = client.get(f"/customers/{customer_id}")
    assert response.status_code == 404
