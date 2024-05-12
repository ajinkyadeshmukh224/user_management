# FastAPI User Management

This is a simple FastAPI application for user management, providing CRUD (Create, Read, Update, Delete) operations for user accounts.

## Features

- Create a new user with username, password, email, first name, last name, and role.
- Retrieve an existing user by user ID.
- Update an existing user's information.
- Delete an existing user.

## Technologies Used

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- databases: An async database support for Python.
- Microsoft SQL Server: A relational database management system developed by Microsoft.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/ajinkyadeshmukh224/user_management.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Microsoft SQL Server database and update the `DATABASE_URL` in `main.py` with your connection string.

4. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

## Usage

- Create a new user: `POST /users/`
- Retrieve an existing user: `GET /users/{user_id}`
- Update an existing user: `PUT /users/{user_id}`
- Delete an existing user: `DELETE /users/{user_id}`

## Example

Create a new user:

```bash
curl -X POST "http://localhost:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{
        "Username": "john_doe",
        "PasswordHash": "password123hash",
        "Email": "john@example.com",
        "Role": "user",
        "FirstName": "John",
        "LastName": "Doe"
     }'

