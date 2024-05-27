import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils import crud, models, schemas
from utils.database import Base
from main import app, get_db

from utils.database import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the test database and tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)

def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is user home"}

def test_create_user(test_db):
    response = client.post("/user/create_user", json={"email": "hari@gmail.com", "password": "testpassword"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "hari@gmail.com"
    assert "id" in data

def test_create_user_existing_email(test_db):
    client.post("/user/create_user", json={"email": "hari@gmail.com", "password": "testpassword"})
    response = client.post("/user/create_user", json={"email": "hari@gmail.com", "password": "testpassword"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_read_users(test_db):
    response = client.get("/user/all_users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_user(test_db):
    client.post("/user/create_user", json={"email": "hari@gmail.com", "password": "testpassword"})
    response = client.get("/user/get_user/1")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "hari@gmail.com"

def test_read_nonexistent_user(test_db):
    response = client.get("/user/get_user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_update_user(test_db):
    client.post("/user/create_user", json={"email": "hari@gmail.com", "password": "testpassword"})
    response = client.put("/users/update_user/1", json={"email": "hari@gmail.com", "password": "newpassword"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "hari@gmail.com"

def test_update_nonexistent_user(test_db):
    response = client.put("/users/update_user/999", json={"email": "hari123@gmail.com", "password": "newpassword"})
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_delete_user(test_db):
    client.post("/user/create_user", json={"email": "hari@gmail.com", "password": "testpassword"})
    response = client.delete("/users/delete_user/1")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "hari@gmail.com"

def test_delete_nonexistent_user(test_db):
    response = client.delete("/users/delete_user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
