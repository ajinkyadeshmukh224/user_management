# FastAPI User Management

This is a simple FastAPI application for user management, providing CRUD (Create, Read, Update, Delete) operations for user accounts.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
  - [Clone Repository](#clone-repository)
  - [Install Dependencies](#install-dependencies)
  - [Database Configuration](#database-configuration)
  - [Run the Application](#run-the-application)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)


## Overview

Provide a brief overview of the project, explaining its purpose and functionality. Mention the technology stack used, such as FastAPI, SQLAlchemy, etc. You can also include any additional context or background information.

## Features

List the key features or functionalities of the application. This can include things like user management, item management, CRUD operations, authentication, authorization, etc.

## Setup

### Clone Repository

1. **Clone Repository**: Clone this repository to your local machine.
   ```bash
   https://github.com/ajinkyadeshmukh224/user_management.git


2. If not possible to clone create with name `user_management` and copy paste or write code from repo


3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Microsoft SQL Server database and update the `DATABASE_URL` and `DATABASE_NAME` in `main.py` with your connection string.


5. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

6. Access Swagger Docs

    ```bash
   http://127.0.0.1:8000/docs
   ```


## Usage

- Create new User: `POST /users/create_user`

- List All Users: `GET /users/all_users`

- Retrieve a list of users with optional pagination. 
  Get User by ID: `GET /users/get_user/{user_id}`

- Update User: `POST /users/update_user/{user_id}`

- Delete User: `DELETE /users/delete_user/{user_id}`


## Example

Create a new user:

```bash
curl -X 'POST' \
      'http://127.0.0.1:8000/user/create_user' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "email": "xyz@gmail.com",
      "password": "xyz123"
    }'
 ```
	 
List All Users:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/user/all_users' \
  -H 'accept: application/json'
 ```
  
Retrieve a list of users with optional pagination. Get User by ID:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/user/get_user/1' \
  -H 'accept: application/json'
 ```

Update User:

```bash
curl -X 'PUT' \
      'http://127.0.0.1:8000/users/update_user/4' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "email": "xyz123@gmail.com",
      "password": "xyz123"
    }'
 ```

Delete User:

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/users/delete_user/4' \
  -H 'accept: application/json'
 ```

## Dependencies

```
fastapi
sqlalchemy
pydantic
pyodbc
uvicorn
```
